# Human
    # Warrior
    # Mage


class Human:
    def __init__(self, name, gender):
        self.name = name
        self.health = 100
        self.strength = 50
        self.is_male = gender
    
    def attack(self, enemy):
        print(f"{self.name} makes a generic attack to {enemy.name} for -10 hp")
        enemy.health -= 10
        print(f"now {enemy.name} has {enemy.health} HP left")



# print(human2.name)
# print(human1.name)



