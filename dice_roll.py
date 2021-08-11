import random

def dice():
    return random.randrange(1, 7)
    
for _ in range(1):
    print(dice())