# Pour pouvoir matérialiser les matières

# Ajouter le typage
from models.professor import Professor


class Topic:
    def __init__(self, name: str, professor: Professor, min_hours: int, max_hours: int):
        self.name = name
        self.professor = professor
        self.min_hours = min_hours
        self.max_hours = max_hours
