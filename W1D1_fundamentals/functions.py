#  FUNCTIONS
# a set of instructions
# ! ALL functions ALWAYS return something

# print(print("hello"))

# verbs
def greeting():
    print("hello there!")
    return "hello"

# print("i'm here!")
# call / invoke the function
# greeting()

# parameters
def say_hello(some_name):
    print("hello " + some_name)

# anything you send to the fucntion is an argument
say_hello("bob")
say_hello("alice")
say_hello("Carter")

def add(a,b):	# function name: 'add', parameters: a and b
    sum = a + b	# process
    return sum	# return value: sum

print(add(1,5))
print(add(4,5))
print(add(66,-1))

# ==================
print("================")

my_list = [22,33,455,75]

def say_times(name, num_times):
    # print(name, name)
    for x in range(num_times):
        print(x)
        if x <= 3:
            print(f"cool your name is {name}")

say_times(num_times=10, name="bob" )


