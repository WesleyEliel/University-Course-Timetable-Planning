class ProfGenerator:
    def __init__(self, quantity: int):
        self.profs_quantity = quantity

    def generate_profs(self):
        return [f"Salle_{index}" for index in range(1, self.profs_quantity)]
