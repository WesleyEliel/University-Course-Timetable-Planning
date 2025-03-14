# -*- coding: utf-8 -*-

import json

from data_initializers.real_problem_initializer import initialize
from scheduler.scheduler import Scheduler

# Initialiser le résolveur
scheduler = Scheduler()

# Initializer les données pour le problème
data = initialize()

# Affichage des données et demande d' approbation de l' utilisateur
print('\n\n\n')

print(json.dumps(data, sort_keys=True, indent=2))

print('\n\n\n')

# Processus d' approbation
_continue = False

while not _continue:
    var = input("Après avoir vu les données générées, voulez vous continuer ? (Oui/Non): ")
    _continue = var.upper() in ["OUI", "O"]

# Lancement du processus d' optimisation

# Ajout des Créneaux

for t_name in data["timeslots"]:
    t_split = t_name.split("_")
    scheduler.add_timeslot(t_name, int(t_split[-2]), int(t_split[-1]))


print(scheduler.timeslots, 99999)
# Ajout des Salles et leur disponibilités

for r_name in data["rooms"]:
    scheduler.add_room(r_name)
    # Add availability timeslots
    for t_name in data["rooms_availability"][r_name]:
        scheduler.set_timeslot_as_availability_for_room(room_name=r_name, timeslot_name=t_name)

# Ajout des Professeurs et leur disponibilités

## Ensemble des professeurs

for p_name in data["profs"]:
    scheduler.add_professor(p_name)
    # Ajout des créneaux de disponibilité de chaque prof
    for t_name in data["profs_availability"][p_name]:
        scheduler.set_timeslot_as_availability_for_prof(professor_name=p_name, timeslot_name=t_name)

# Ajouter des matières
for topic in data["topics"]:
    scheduler.add_topic(topic['name'], topic["assigned_prof"], topic["min_hours"], topic["max_hours"])

# Preparation de la résolution
scheduler.prepare_variables()
scheduler.add_constraints()
scheduler.define_objective()

# Resolution
scheduler.solve()
