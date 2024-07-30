# OOP

dog_one = {
    'name' : 'Zoy',
    'age' : 4,
    'breed' : "GSP"
}

dog_two = {
    'name' : 'Spot',
    'age' : 8,
    "breed": "black lab"
}
# dog_two['name']

# ----- create a Class -----
class Dog:
    # constructor - creates defaults and builds the istance
    def __init__(self, name, age, breed, wanna_eat=False):
        # attributes - what a class HAS
        self.name = name
        self.age = age
        self.breed = breed
        self.is_hungry = wanna_eat
        self.can_swim = True
    
    # methods - actions (aka functions)
    def bark(self):
        print(f"WOOF WOOF {self.name}")
        return self

    def eats(self):
        if self.is_hungry == True:
            print("OM NOM NOM!! YUMMY")
            self.is_hungry = False
        else:
            print("WOOF I'm FULL!!!!")
            self.bark()
    

# create an instance of the Dog class
first_doggo_instance = Dog("Michi", 10, "pug")

# print( first_doggo_instance.bark() )
first_doggo_instance.bark().bark().bark()


# print(first_doggo_instance.is_hungry)

# first_doggo_instance.eats()


# print(first_doggo_instance.name)
# print(first_doggo_instance.age)
# print(first_doggo_instance.breed)

# first_doggo_instance.bark()
# first_doggo_instance.bark()
# first_doggo_instance.bark()
# first_doggo_instance.bark()

# print(first_doggo_instance.is_hungry)
# first_doggo_instance.eats()
# print(first_doggo_instance.is_hungry)

# print("-------------")
# second_doggo_instance = Dog("Goofy", 12, "Coonhound", False)
# # print(second_doggo_instance.name)
# # print(second_doggo_instance.age)
# # print(second_doggo_instance.breed)
# first_doggo_instance.bark()
# second_doggo_instance.bark()