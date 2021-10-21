import random

def diceRoller(numDice, diceType, modifier):
    sum = 0
    for i in range(1, numDice):
        sum+= random.randrange(diceType)
    return sum + modifier

#4d6 + 3
print("4d6 + 3")
print(diceRoller(4,6,3))
#2d8 + 1
print("2d8 + 1")
print(diceRoller(2,8,1))
#3d4 - 2
print("3d4 - 1")
print(diceRoller(3,4,-1))