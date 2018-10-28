import random

x, y = int(5), int(6)
z = random.randint(1, 1000)
v = random.randint(1, 1000)
while x == 5 and y == 6:
    print(x + z, y + v)
    break