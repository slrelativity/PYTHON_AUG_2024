from inheritance import Human
from Warrior import Warrior

human1 = Human("bob", True)
human2 = Human("Alice", False)

human2.attack(human1)

warrior_name = input("what is your Warrior's name?")

warrior1 = Warrior(warrior_name, True)
print(warrior1.name)
print(warrior1.health)

warrior1.attack(human1)