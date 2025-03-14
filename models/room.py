# -*- coding: utf-8 -*-

# Pour pouvoir matérialiser les salles

from models.timeslot import TimeSlot


class Room:
    def __init__(self, name: str):
        self.name = name
        self.availability = set()

    def __str__(self):
        return f"{self.name}"

    def add_availability(self, timeslot: TimeSlot):
        # Permet d' ajouter un crenau de disponibilité
        self.availability.add(timeslot)
