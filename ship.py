import random
from part import Part

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Coque": Part("Coque", "Bois"),
            "Mât": Part("Mât", "Bois"),
            "Gouvernail": Part("Gouvernail", "Bois")
        }
        self.history = []

    def get_parts(self):
        return self.__parts

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            old = str(self.__parts[part_name])
            self.__parts[part_name] = new_part
            self.history.append(f"Remplacement: {old} -> {new_part}")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Modif: {part_name} est passé en {new_material}")

    def random_event(self):
        events = ["Tempête", "Attaque de pirates", "Usure"]
        event = random.choice(events)
        target = random.choice(list(self.__parts.keys()))
        self.change_part(target, "Abîmé")
        return f"{event} ! {target} est endommagé."

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed