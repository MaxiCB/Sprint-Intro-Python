# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
# Iterate through all humans
for i in humans:
    # Check if the first char in the string is 'D'
    if i.name[0] == "D":
        # If so append the human's name to the a array
        a.append(i.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
# Iterate over all humans
for i in humans:
    # Check the last char in the name to 'e'
    if i.name[len(i.name) - 1] == "e":
        # If the last char is 'e' append it to b array
        b.append(i.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
# Iterate over all humans
for i in humans:
    # Check if the first char is between 'C' and 'G'
    if (i.name[0] >= 'C') and (i.name[0] <= 'G'):
        # If so append the name to c array
        c.append(i.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
# Iterate over all humans
for i in humans:
    # Add 10 to all of the humans age and append it to d array
    d.append(i.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
# Iterate over all humans
for i in humans:
    # Append the name and age to the e array in ('Name'-Age) format
    e.append(i.name + "-" + str(i.age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
# Iterate over all humans
for i in humans:
    # Check if human age is between 27 && 32
    if (i.age >= 27) and (i.age <= 32):
        # Create a tuple with the humans name and age
        person_tuple = i.name, i.age
        # Append the tuple to the f array
        f.append(person_tuple)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
# Iterate over all humans
for i in humans:
    # Convert names to uppercase && add 5 to age
    new_name = i.name.upper()
    new_age = i.age + 5
    # Create a new Human using the modified values
    new_human = Human(new_name, new_age)
    # Append the new Human to g array
    g.append(new_human)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
# Iterate over all humans
for i in humans:
    # Using the math import find the square root of the Human age
    sqr_age = math.sqrt(i.age)
    # Append the square root to the h array
    h.append(sqr_age)
print(h)
