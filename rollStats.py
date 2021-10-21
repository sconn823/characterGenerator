import random

#Taking a list of 4 numbers, return a list of the three non-lowest numbers
def dropTheLowest(inputList):
    sum = 0
    droppedLowest = sorted(inputList)[1:len(inputList)]
    for i in range(0, len(droppedLowest)):
        sum += droppedLowest[i]
    return sum

def rollStatsTraditional():
    stats = []
    diceRolls = []
    #For each of the abilities
    for i in range(0, 6):
        #For each of the four dice being rolled
        for i in range(0,4):
            diceRolls.append(random.randrange(1,6))
        
        stats.append(dropTheLowest(diceRolls))
        diceRolls = []
    
    return stats
    

print(rollStatsTraditional())