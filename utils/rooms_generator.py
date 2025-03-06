class RoomGenerator:
    def __init__(self, quantity: int):
        self.rooms_quantity = quantity

    def generate_rooms(self):
        return [f"Salle_{index}" for index in range(1, self.rooms_quantity)]
