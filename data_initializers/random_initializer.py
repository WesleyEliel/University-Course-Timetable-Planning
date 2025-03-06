########################################################################################################################

# Créneaux
import random

from utils.proofs_generator import ProfGenerator
from utils.rooms_generator import RoomGenerator
from utils.timeslots_generator import TimeSlotGenerator
from utils.utils import random_choices_from_list

available_topics = [
    {
        "name": "R.O et I.A",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 16
    },
    {
        "name": "Maths pour l' informatique",
        "assigned_prof": "",
        "min_hours": 30,
        "max_hours": 40
    },
    {
        "name": "Administration Réseaux",
        "assigned_prof": "",
        "min_hours": 30,
        "max_hours": 40
    },
    {
        "name": "Sécurité Web & Mobile",
        "assigned_prof": "",
        "min_hours": 20,
        "max_hours": 20
    },
    {
        "name": "Thermodynamique et Transfert de Chaleur",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 20
    },
    {
        "name": "Architecture des réseaux d' ordinateurs",
        "assigned_prof": "",
        "min_hours": 20,
        "max_hours": 20
    },
    {
        "name": "Électricité et Électrostatique Générale",
        "assigned_prof": "",
        "min_hours": 20,
        "max_hours": 24
    },
    {
        "name": "Méthodes d' analyse et de Spécification",
        "assigned_prof": "",
        "min_hours": 20,
        "max_hours": 30
    },
    {
        "name": "Architecture Logicielle",
        "assigned_prof": "",
        "min_hours": 16,
        "max_hours": 20
    },
    {
        "name": "Anglais Technique",
        "assigned_prof": "",
        "min_hours": 8,
        "max_hours": 16
    },
    {
        "name": "Déontologie et TIC",
        "assigned_prof": "",
        "min_hours": 4,
        "max_hours": 10
    },
    {
        "name": "Semi Conducteurs et Électronique",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 24
    },
    {
        "name": "Introduction à la Blockchain",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 20
    },
    {
        "name": "Introduction à l' IOT",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 24
    },
    {
        "name": "Gestion de Projet",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 16
    },
    {
        "name": "Traitement d' Image",
        "assigned_prof": "",
        "min_hours": 16,
        "max_hours": 30
    },
    {
        "name": "Méthodologies de Rédaction de Mémoire",
        "assigned_prof": "",
        "min_hours": 8,
        "max_hours": 12
    },
    {
        "name": "Cryptographie",
        "assigned_prof": "",
        "min_hours": 12,
        "max_hours": 20
    },
    {
        "name": "DevSecOps",
        "assigned_prof": "",
        "min_hours": 16,
        "max_hours": 30
    },
    {
        "name": "Interfaces Homme-Machine",
        "assigned_prof": "",
        "min_hours": 14,
        "max_hours": 30
    },
]


def initialize():
    timeslots = TimeSlotGenerator("27-01-2025", "09-03-2025").generate_slots()

    ########################################################################################################################

    # Salles et leur disponibilités

    ## Ensemble des salles
    rooms = RoomGenerator(9).generate_rooms()

    rooms_availability = {room: random_choices_from_list(timeslots, random.randint(len(rooms), len(timeslots))) for room
                          in
                          rooms}

    ########################################################################################################################

    # Professeurs et leur disponibilités

    ## Ensemble des professeurs
    profs = ProfGenerator(6).generate_profs()
    profs_availability = {room: random_choices_from_list(timeslots, random.randint(len(profs), len(timeslots))) for room
                          in
                          rooms}

    ########################################################################################################################

    # Matières

    topics = [{**item, "assigned_prof": random.choice(profs)} for item in
              random_choices_from_list(available_topics, random.randint(len(profs), len(available_topics)))]

    ########################################################################################################################
    return {
        "timeslots": timeslots,
        "rooms": rooms,
        "rooms_availability": rooms_availability,
        "profs": profs,
        "profs_availability": profs_availability,
        "topics": topics,
    }
