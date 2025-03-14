# -*- coding: utf-8 -*-

from scheduler.scheduler import Scheduler

# 🏗️ Initialize Scheduler
scheduler = Scheduler()

########################################################################################################################

# Ajouter des Créneaux

## Ensemble des créneaux comme supposé dans la description
timeslots = [
    "Lundi_8_12", "Lundi_14_18",
    "Mardi_8_12", "Mardi_14_18",
    "Mercredi_8_12", "Mercredi_14_18",
    "Jeudi_8_12", "Jeudi_14_18",
    "Vendredi_8_12", "Vendredi_14_18",
    "Samedi_8_14"
]
for t_name in timeslots:
    _, start, end = t_name.split("_")
    scheduler.add_timeslot(t_name, int(start), int(end))

########################################################################################################################

# Ajouter des Salles et leur disponibilités

## Ensemble des salles
rooms = ["Salle_A", "Salle_B", "Salle_C"]
rooms_availability = {
    # Salle A disponible Lundi toute la journée, Mardi Matin et Mercredi Matin
    "Salle_A": ["Lundi_8_12", "Lundi_14_18", "Mardi_8_12", "Mercredi_8_12"],

    # Salle B disponible Mardi soir, Mercredi soir et Vendredi toute la journée
    "Salle_B": ["Mardi_14_18", "Vendredi_8_12", "Vendredi_14_18", "Mercredi_14_18"],

    # Salle C disponible Jeudi toute la journée et Samedi Matin
    "Salle_C": ["Jeudi_8_12", "Jeudi_14_18", "Samedi_8_14"],
}

for r_name in rooms:
    scheduler.add_room(r_name)
    # Add availability timeslots
    for t_name in rooms_availability[r_name]:
        scheduler.set_timeslot_as_availability_for_room(room_name=r_name, timeslot_name=t_name)

########################################################################################################################

# Ajouter des Professeurs et leur disponibilités

## Ensemble des professeurs
profs = ["Prof_A", "Prof_B", "Prof_C"]
profs_availability = {
    # Prof A disponible Lundi toute la journée, Mardi Matin et Mercredi Matin
    "Prof_A": ["Lundi_8_12", "Lundi_14_18", "Mardi_8_12", "Mercredi_8_12"],

    # Salle B disponible Mardi soir, Mercredi soir et Vendredi toute la journée
    "Prof_B": ["Mardi_14_18", "Vendredi_8_12", "Vendredi_14_18", "Mercredi_14_18"],

    # Salle C disponible Jeudi toute la journée et Samedi Matin
    "Prof_C": ["Jeudi_8_12", "Jeudi_14_18", "Samedi_8_14"],
}
for p_name in profs:
    scheduler.add_professor(p_name)
    # Add availability timeslots
    for t_name in profs_availability[p_name]:
        scheduler.set_timeslot_as_availability_for_prof(professor_name=p_name, timeslot_name=t_name)

########################################################################################################################

# Ajouter des matières
topics = [
    {
        "name": "R.O et I.A",
        "assigned_prof": "Prof_A",
        "min_hours": 12,
        "max_hours": 16
    },
    {
        "name": "Maths pour l' informatique",
        "assigned_prof": "Prof_A",
        "min_hours": 4,
        "max_hours": 8
    },
    {
        "name": "Administration Réseaux",
        "assigned_prof": "Prof_B",
        "min_hours": 4,
        "max_hours": 8
    },
    {
        "name": "Sécurité Web & Mobile",
        "assigned_prof": "Prof_C",
        "min_hours": 4,
        "max_hours": 8
    },
]

for topic in topics:
    scheduler.add_topic(topic['name'], topic["assigned_prof"], topic["min_hours"], topic["max_hours"])

########################################################################################################################

# Prepare and Solve
scheduler.prepare_variables()
scheduler.add_constraints()
scheduler.define_objective()
scheduler.solve()
