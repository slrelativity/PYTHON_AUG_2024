# FUNDAMENTALS
# this is a comment - it does not get read by the interperter 
"""
this is a multi-
line comment
but also look at the color
it's a string!
"""

# Primitive variables

my_float = 3.14
my_name = 'Bob'
my_vote = True
days = 22
vacation = "Italy"

new_string = f"I went on a vacation to {vacation}, I stayed there for {days} days"
# print(new_string)

# print("hello there! " + my_name + " I have " + str(my_float) + " Bitcoints")
my_new_string = f"hello there! {my_name}"
# print(my_new_string)

# Composite types
# Lists aka Arrays in JS

my_nums = [11,22,33,44]
# 0x0ef14
#          0        1        2       3 
names = ["bob", "alice", "carter", "devin"]

names_copy = names # don't do this
true_names_copy = names[:]

# print(names[2])
print(names)
names.pop(2) # remove 

names.append("🦄")

print("NAMES      ---->", names)
print("NAMES_COPY ---->", true_names_copy)

print(names)
# lenght?
print(f"there are {len(names)} things in the list")




# Dictionaries aka Objects in JS
# Key - value pairs
doggo1 = {
    "name" : "Mochi",
    "age" : 6,
    "colors" : ["black", "brown"],
    "is_a_good_boi" : True
}

doggo2 = {
    "name" : "Zoy",
    "age" : 4,
    "colors" : ["gray"],
    "is_a_good_girl" : True
}

doggo2['fav_toy'] = "stuffed 🦆"
print("🐶🐶🐶🐶", doggo2)

if "age" in doggo2:
    print(f"⭐⭐⭐ found age with the name: {doggo2['name']}")
else:
    print("❌❌❌ age is not found")

# remove a key
doggo2.pop("is_a_good_girl")
del doggo2['age']
print(" ------- ", doggo2)


awesome_doggos = [doggo1, doggo2]

# print(awesome_doggos)



# print(doggo1["name"])
# print(doggo1["colors"][0])
# print(doggo.name) # can only do when an instance of a Class


# Tuples
dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)
