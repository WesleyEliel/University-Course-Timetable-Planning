# -*- coding: utf-8 -*-

# Pour pouvoir matérialiser les crénaux horaires

# Todo: Ajouter le typage

class TimeSlot:
    def __init__(self, name: str, start_time: int, end_time: int):
        # Je vais devoir renchérir ça en ajoutant un paramètre de date, 
        # Par la suite un créneau horaire sera déterminé par Une date, une heure de début et une heure de fin
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def duration(self):
        return self.end_time - self.start_time
