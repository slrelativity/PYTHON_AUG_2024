from inheritance import Human

class Warrior(Human):
    def __init__(self, name, gender):
        super().__init__(name, gender)
    
    def attack(self, enemy):
        print(f"WARRIOR {self.name} makes a STRONG attack to {enemy.name} for -30 hp")
        enemy.health -= 30
        print(f"now {enemy.name} has {enemy.health} HP left")


