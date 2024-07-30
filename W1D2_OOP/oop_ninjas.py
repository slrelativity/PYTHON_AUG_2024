# REVIEW  OOP, classes, attributes, methods
# TODO classmethod, staticmethod

class Ninja:

    # a class method or attribute belong to the CLASS - NOT the instance
    all_ninjas = []

    #Constructor (aka attributes --------------)
    def __init__(self, name_param, weapon_param, hp, clan, master, age_param):
        if Ninja.check_age(age_param):
            self.name = name_param
            self.weapon = weapon_param
            self.health = hp
            self.age = age_param
            self.clan = clan
            self.is_sensei = master
            Ninja.all_ninjas.append(self)
        else:
            return

    # mehtods ---------------
    def display_stats(self):
        print(f"{self.name} has a {self.weapon} with {self.health} HP and is part of the {self.clan} clan")

    def eat_pizza(self, amount):
        self.health += amount
        print(f"{self.name} ate a pizza for +{amount} HP and they now have {self.health} HP")

    def attack(self, target):
        print(f"{self.name} attacks {target.name}")
        target.health -= 10
        print(f"after the attack, {target.name} now has {target.health} HP remaining")
        return self
    
    @classmethod
    def have_party(cls):
        print(cls.all_ninjas)
        for one_ninja in cls.all_ninjas :
            one_ninja.eat_pizza(40)

    @staticmethod
    def check_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
            print("you are not old enought to enter the dojo")
        return is_valid

    # extra
    # __main__ - it ran directly from this file
    # __repr__ - overwrites the <__main__.Ninja object at 0x000002530A8CAD20>
    # string representation of the instance
    # def __repr__(self) -> str:
    #     return f"this is {self.name}"

ninja_1 = Ninja("Donatello", "staff", 100, "TMNT", False, 17)
ninja_3 = Ninja("Splinter", "knifes", 200, "Foot Clan", True, 33)
# ninja_1.display_stats()
# ninja_1.eat_pizza(20)
# ninja_1.display_stats()

ninja_2 = Ninja("Raphael", "sai", 90, "TMNT", False, 20)
# ninja_2.display_stats()

ninja_2.attack(ninja_3).attack(ninja_3).attack(ninja_3).attack(ninja_3)

# ninja_1.attack(ninja_2)
# ninja_1.attack(ninja_2)

# Ninja.have_party()
print(Ninja.all_ninjas)
