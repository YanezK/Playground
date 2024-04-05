class Monster:
    def __init__(self, name):
        print("Creating a monster")
        self.name = name

    def attack(self):
        print(f"Monster {self.name}, is attacking")

class Shark(Monster):
    def __init__(self, number_of_teeths):
        # Monster.__init__(self, "Shark Name")
        super().__init__("Shark Name")
        print("Created a Shark")

    def attack(self):
        print("A shark is attacking")


# monster = Monster("Monster")
# monster.attack()

shark = Shark(number_of_teeths = 14)
shark.attack()