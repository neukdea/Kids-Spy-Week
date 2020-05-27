import random

item1 = open('english-adjectives.txt', 'r')
first = random.choice(item1.readlines()).rstrip()
item2 = open('Animals.txt', 'r')
second = random.choice(item2.readlines())

print("Your code name is{} {}".format(first, second))