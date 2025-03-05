from typing import List, Union

from ortools.sat.python import cp_model

from models.professor import Professor
from models.room import Room
from models.timeslot import TimeSlot
from models.topics import Topic


class Scheduler:
    def __init__(self):
        self.timeslots: List[TimeSlot] = []
        self.rooms: List[Room] = []
        self.professors: List[Professor] = []
        self.topics: List[Topic] = []
        self.model = cp_model.CpModel()
        self.X = {}

    def __str__(self):
        # Todo: surcharger la methode pour afficher un récapitulatif des données pour l' optimisation
        return super(Scheduler, self).__str__()

    def add_timeslot(self, name: str, start: int, end: int):
        """
        Permet d' ajouter un créneaux horaire à la liste des créneaux disponible
        """
        self.timeslots.append(TimeSlot(name, start, end))

    def add_room(self, room: Union[str, Room]):
        """
        Permet d' ajouter une salle à la liste des professeurs disponible
        """
        if type(room) is not Room:
            room = Room(name=room)

        self.rooms.append(room)

    def add_professor(self, prof: str):
        """
        Permet d' ajouter un professeur à la liste des professeurs disponible
        """
        if type(prof) is not Professor:
            prof = Professor(name=prof)

        self.professors.append(prof)

    def add_topic(self, name, professor_name: str, min_hours: int, max_hours: int):
        """
        Permet d' ajouter une matière à la liste des matières à programmer
        Avec le nombre d' heures min qu' on veut programmer et le maximum
        """
        # Retrouver le professeur dont le nom a été renseigné
        # Il faut au préalable qu' il soit renseigné dans la liste des profs disponible
        professor = self.get_prof_by_name(professor_name)

        # Si le professeur est retrouvé, ajouter la matière en assignat
        if professor:
            self.topics.append(Topic(name=name, professor=professor, min_hours=min_hours, max_hours=max_hours))

    def get_prof_by_name(self, professor_name: str) -> Union[Professor, None]:
        """
        Permet de retrouver l' objet Professeur associé au nom d' un professeur
        Il faut au préalable que l' object ai été créé et ajouté à la list des profs disponible avec add_professor
        """
        return next((p for p in self.professors if p.name == professor_name), None)

    def get_room_by_name(self, room_name: str) -> Union[Room, None]:
        """
        Permet de retrouver l' objet Room associé au nom d' une classe
        Il faut au préalable que l' object ai été créé et ajouté à la list des classes disponible avec add_room
        """
        return next((r for r in self.rooms if r.name == room_name), None)

    def get_timeslot_by_name(self, timeslot_name: str) -> Union[TimeSlot, None]:
        """
        Permet de retrouver l' objet Timeslot associé au nom d' un créneau
        Il faut au préalable que l' object ai été créé et ajouté à la list des créneaux disponible avec add_timeslot
        """
        return next((t for t in self.timeslots if t.name == timeslot_name), None)

    def set_timeslot_as_availability_for_prof(self, professor_name: str, timeslot_name: str):
        """
        Permet d' ajouter un créneaux comme disponible pour un prof
        """
        prof = self.get_prof_by_name(professor_name=professor_name)
        if prof:
            timeslot = self.get_timeslot_by_name(timeslot_name=timeslot_name)
            if timeslot:
                prof.add_availability(timeslot=timeslot)
                return True
        return False

    def set_timeslot_as_availability_for_room(self, room_name, timeslot_name):
        """
        Permet d' ajouter un créneaux comme disponible pour une salle
        """
        room = self.get_room_by_name(room_name=room_name)
        if room:
            timeslot = self.get_timeslot_by_name(timeslot_name=timeslot_name)
            if timeslot:
                room.add_availability(timeslot=timeslot)
                return True
        return False

    def prepare_variables(self):
        """
        Permet d' établir la liste des variable en fonction des objects créés
        quand l' utilisateur renseignait les données d' optimisation
        """
        for topic in self.topics:
            for room in self.rooms:
                for professor in self.professors:
                    for timeslot in self.timeslots:
                        self.X[topic.name, room.name, professor.name, timeslot.name] = self.model.new_bool_var(
                            f"X_{topic.name}_{room.name}_{professor.name}_{timeslot.name}"
                        )

    def add_constraints(self):
        """
        Ajout des contraintes
        """
        # Une salle ne peut accueillir qu’un seul cours à un moment donné
        for room in self.rooms:
            for timeslot in self.timeslots:
                self.model.Add(sum(
                    self.X[s.name, room.name, p.name, timeslot.name]
                    for s in self.topics for p in self.professors
                ) <= 1)

        # Une salle ne peut accueillir qu’un seul cours à un moment donné
        for professor in self.professors:
            for timeslot in self.timeslots:
                self.model.Add(sum(
                    self.X[s.name, r.name, professor.name, timeslot.name]
                    for s in self.topics for r in self.rooms
                ) <= 1)

        # Un professeur ne peut donner un cours que s’ il est assigné à la matière
        for topic in self.topics:
            for room in self.rooms:
                for professor in self.professors:
                    if professor != topic.professor:
                        for timeslot in self.timeslots:
                            self.model.Add(self.X[topic.name, room.name, professor.name, timeslot.name] == 0)

        # Respect des disponibilités des salles
        # Si une salle n' est pas disponible sur un crenaux, alors il ne sert a rien même de l' évaluer,
        # aucun cours ne peut pas avoir lieu dans cette salle à ce crenaux Xm,s,s,t prends la valeur 0
        for room in self.rooms:
            for timeslot in self.timeslots:
                if timeslot not in room.availability:
                    for topic in self.topics:
                        for professor in self.professors:
                            self.model.Add(self.X[topic.name, room.name, professor.name, timeslot.name] == 0)

        # Respect des disponibilités des professeurs
        # Si un prof n' est pas disponible sur un crenaux, alors il ne sert a rien même de l' évaluer,
        # il ne peut pas faire un cours à ce crenaux Xm,s,s,t prends la valeur 0
        for professor in self.professors:
            for timeslot in self.timeslots:
                if timeslot not in professor.availability:
                    for topic in self.topics:
                        for room in self.rooms:
                            self.model.Add(self.X[topic.name, room.name, professor.name, timeslot.name] == 0)

        # Chaque matière doit respecter son minimum et maximum d' heures sur la période définie
        for topic in self.topics:
            total_hours = sum(
                self.X[topic.name, r.name, p.name, t.name] * t.duration()
                for r in self.rooms for p in self.professors for t in self.timeslots
            )
            self.model.Add(total_hours >= topic.min_hours)
            self.model.Add(total_hours <= topic.max_hours)

    def define_objective(self):
        """
        Permet de définir la fonction objective
        """
        # Fonction objective liée à la maximisation du nombre de cours programmé
        self.model.Maximize(sum(self.X[s.name, r.name, p.name, t.name]
                                for s in self.topics for r in self.rooms
                                for p in self.professors for t in self.timeslots))

    def solve(self):
        solver = cp_model.CpSolver()
        status = solver.Solve(self.model)

        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            print(f"\nUne solution trouvé : ( {'Solution Optimale' if cp_model.OPTIMAL else 'Solution non optimale'} ) \n")
            for topic in self.topics:
                for room in self.rooms:
                    for professor in self.professors:
                        for timeslot in self.timeslots:
                            if solver.Value(self.X[topic.name, room.name, professor.name, timeslot.name]) == 1:
                                day, start_hour, end_hour = timeslot.name.split('_')
                                print(
                                    f"{topic.name} planifié pour {professor.name} dans la salle {room.name} sur le créneaux {day} de {start_hour}h à {end_hour}h")
        else:
            print("Aucune solution")
