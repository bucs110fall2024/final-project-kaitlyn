import random

class Order:
    def __init__(self):
        self.orders = ["Salmon Onigiri", "Mentaiko Onigiri", "Plum Onigiri", "Tempura Onigiri"]
        self.current_order = ""
        self.combinations = {
            ("sea_plate", "rice_plate", "salmon_plate"): "Salmon Onigiri",
            ("sea_plate", "rice_plate", "mentaiko_plate"): "Mentaiko Onigiri",
            ("sea_plate", "rice_plate", "temp_plate"): "Tempura Onigiri",
            ("sea_plate", "rice_plate", "plum_plate"): "Plum Onigiri"
        }
    
    def generate_order(self):
        self.current_order = random.choice(list(self.combinations.values()))
        return f"I would like a {self.current_order}"
    
    def get_correct_combination(self):
        for combo, order in self.combinations.items():
            if order == self.current_order:
                return combo
        return ()
