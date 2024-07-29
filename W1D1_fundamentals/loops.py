#  LOOPS

# For loops

# for _iterator_ in _collection_ :

# range() - function that returns a sequence of numbers
# range(start, stop, step)
    # start - inclusive - optional - default 0
    # stop - EXCLUSIVE, required
    # step - optional -incement value (+/-)

# 1-10
for num in range(1, 10 + 1):
    print(num)

# 1-10 every 2
for x in range(1, 11, 2):
    print(x)

print("----------")

# 100 - 1 down by 20
for i in range(100, 0, -1):
    print(i)

x = 10
y = 20

for some_iterator in range(x, y+1):
    print(some_iterator)

print("=======")
print(range(2,10))
print("range(2,10)")

for letter in "hello":
    print(letter)


anime_list = ["Attack on Titan", "One Piece", "Bog O", "hunter x hunter"]

for single_anime in anime_list:
    print(single_anime)

for i in range(len(anime_list)):
    print(i+1, anime_list[i])

for single in range(int(len(anime_list) / 2)):
    print(single, anime_list[single])

print(4/2)

# ---- dictionaries ----

bob_dict = {
    "name" : "bob",
    "age" :20,
    "fav_food" : "🍕"
}

for each_key in bob_dict:
    # print(each_key, bob_dict[each_key])
    print(f"key: {each_key}, value: {bob_dict[each_key]}")

capitals = {
    "Washington": "Olympia",
    "California": "Sacramento",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Texas": "Austin",
    "Oklahoma": "Oklahoma City",
    "Virginia": "Richmond",
}

for state in capitals:
    print(state, capitals[state])
print("===============")
for val in capitals.values():
    print(val)

for key in capitals.keys():
    print(key)

for x,y in capitals.items():
    print(f"{x}'s capital is {y}")
# for x in capitals.items():
#     print(f"{x[0]}'s capital is {x[1]}")
