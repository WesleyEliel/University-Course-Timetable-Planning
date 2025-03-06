from data_initializers.initialize import initialize
from scheduler.scheduler import Scheduler

# 🏗️ Initialize Scheduler
scheduler = Scheduler()
data = initialize()
print('\n\n\n')

print(data)

print('\n\n\n')

_continue = False

while not _continue:
    var = input("Après avoir vu les données aléatoires générés, voulez vous continuer ? (Oui/Non): ")
    _continue = var.upper() in ["OUI", "O"]

########################################################################################################################

# Ajouter des Créneaux

for t_name in data["timeslots"]:
    t_split = t_name.split("_")
    scheduler.add_timeslot(t_name, int(t_split[-2]), int(t_split[-1]))

########################################################################################################################

# Ajouter des Salles et leur disponibilités

for r_name in data["rooms"]:
    scheduler.add_room(r_name)
    # Add availability timeslots
    for t_name in data["rooms_availability"][r_name]:
        scheduler.set_timeslot_as_availability_for_room(room_name=r_name, timeslot_name=t_name)

########################################################################################################################

# Ajouter des Professeurs et leur disponibilités

## Ensemble des professeurs

for p_name in data["profs"]:
    scheduler.add_professor(p_name)
    # Add availability timeslots
    for t_name in data["profs_availability"][p_name]:
        scheduler.set_timeslot_as_availability_for_prof(professor_name=p_name, timeslot_name=t_name)

########################################################################################################################

# Ajouter des matières
for topic in data["topics"]:
    scheduler.add_topic(topic['name'], topic["assigned_prof"], topic["min_hours"], topic["max_hours"])

########################################################################################################################

# Prepare and Solve
scheduler.prepare_variables()
scheduler.add_constraints()
scheduler.define_objective()
scheduler.solve()
