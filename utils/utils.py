import random
from typing import List


def random_choices_from_list(lst: List, len_of_choices: int):
    if len_of_choices > len(lst):
        return lst

    num_choices = random.randint(len_of_choices, len(lst))  # Choisir un nombre aléatoire d'éléments
    return random.sample(lst, num_choices)
