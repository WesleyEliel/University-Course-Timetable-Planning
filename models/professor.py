# -*- coding: utf-8 -*-

# Pour pouvoir matérialiser les professeurs / enseignants

from models.timeslot import TimeSlot


class Professor:
    def __init__(self, name: str):
        self.name = name
        self.availability = set()

    def __str__(self):
        return f"{self.name}"

    def add_availability(self, timeslot: TimeSlot):
        # Permet ajouter un créneau de disponibilité
        self.availability.add(timeslot)
