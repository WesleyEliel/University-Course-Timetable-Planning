# -*- coding: utf-8 -*-

from utils.timeslots_generator import TimeSlotGenerator

available_topics = [
    {
        "name": "R.O et I.A",
        "assigned_prof": "Dr_Ra_HOUN",
        "min_hours": 8,
        "max_hours": 12
    },
    {
        "name": "Méthodes d' analyse et de conception",
        "assigned_prof": "Dr_Ra_HOUN",
        "min_hours": 4,
        "max_hours": 4
    },
    {
        "name": "Architecture et spécifications des logiciels ",
        "assigned_prof": "M_Ars_LAW",
        "min_hours": 4,
        "max_hours": 4
    },
    {
        "name": "Introduction à la Cryptographie",
        "assigned_prof": "Prof_Eug_EZIN",
        "min_hours": 4,
        "max_hours": 4
    },
    {
        "name": "Gestion de Projets Informatiques",
        "assigned_prof": "Dr_Arn_AHOUAN",
        "min_hours": 8,
        "max_hours": 12
    },
    {
        "name": "Dev Web et Mobile",
        "assigned_prof": "M_Er_ADJE",
        "min_hours": 4,
        "max_hours": 6
    },
]


def initialize(start_time: str = "13-01-2025", end_time: str = "19-01-2025", room_quantity: int = 2,
               proof_quantity: int = 6):
    """
    Permet d 'initialiser des données random sur une certaine période de temps

    params:
        start_time: str, Ex 27-01-2025
        end_time: str, Ex 09-03-2025
        room_quantity: int,
        proof_quantity: int,

    """
    timeslots = TimeSlotGenerator(start_time, end_time).generate_slots()

    print(timeslots)
    ###################################################################################################################

    # Salles et leur disponibilités

    ## Ensemble des salles
    rooms = ["Salle_TDD", "En_ligne"]

    rooms_availability = {
        "Salle_TDD": [],  # Salle TDD
        "En_ligne": [],  # En ligne
    }

    ###################################################################################################################

    # Professeurs et leur disponibilités

    ## Ensemble des professeurs
    profs = ["M_Ars_LAW", "Prof_Eug_EZIN", "Dr_Arn_AHOUAN", "M_Er_ADJE"]

    # Les données de temps généré ressemblent à ceci
    # x = ['Lundi_13-01-2025_08_13', 'Lundi_13-01-2025_14_18', 'Mardi_14-01-2025_08_13', 'Mardi_14-01-2025_14_18',
    #      'Mercredi_15-01-2025_08_13', 'Mercredi_15-01-2025_14_18', 'Jeudi_16-01-2025_08_13', 'Jeudi_16-01-2025_14_18',
    #      'Vendredi_17-01-2025_08_13', 'Vendredi_17-01-2025_14_18', 'Samedi_18-01-2025_8_14']

    profs_availability = {
        # Toute la journée du vendredi
        "M_Ars_LAW": ['Vendredi_17-01-2025_08_13', 'Vendredi_17-01-2025_14_18'],

        # Seulement Jeudi soir
        "Prof_Eug_EZIN": ['Jeudi_16-01-2025_08_13'],

        # Mardi matin, Jeudi soir et Vendredi soir
        "Dr_Ra_HOUN": ['Mardi_14-01-2025_08_13', 'Jeudi_16-01-2025_14_18'],

        # Mardi toute la journée et Mercredi matin
        "Dr_Arn_AHOUAN": ['Mardi_14-01-2025_08_13', 'Mardi_14-01-2025_14_18', 'Mercredi_15-01-2025_08_13'],

        # Lundi Matin et vendredi toute la journée
        "M_Er_ADJE": ['Lundi_13-01-2025_08_13', 'Vendredi_17-01-2025_08_13', 'Vendredi_17-01-2025_14_18', ]
    }

    return {
        "timeslots": timeslots,
        "rooms": rooms,
        "rooms_availability": rooms_availability,
        "profs": profs,
        "profs_availability": profs_availability,
        "topics": available_topics,
    }
