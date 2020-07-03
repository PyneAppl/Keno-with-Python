# The actual Keno Game
from random import randint
# Variables
sameNumb = 0
# Keno selecting the numbers
def keno():
    xs = []
    while len(xs) != 20:
        num = randint(1, 80)
        try:
            xs.index(num)
        except ValueError:
            xs.append(num)
    return xs
# Turns the user input (str) into a list (int)
def slap(input):
    slap = []
    xs = input.split()
    for i in xs:
        slap.append(int(i))
    return slap
# Function that defines the winnings of the Keno game
def winnings():
    if len(zs) == 1:
        if sameNumb == 1:
            return 3
        else:
            return 0
    elif len(zs) == 2:
        if sameNumb == 2:
            return 12
        else:
            return 0
    elif len(zs) == 3:
        if sameNumb == 2:
            return 1
        elif sameNumb == 3:
            return 44
        else:
            return 0
    elif len(zs) == 4:
        if sameNumb == 2:
            return 1
        elif sameNumb == 3:
            return 4
        elif sameNumb == 4:
            return 120
        else:
            return 0
    elif len(zs) == 5:
        if sameNumb == 3:
            return 2
        elif sameNumb == 4:
            return 14
        elif sameNumb == 5:
            return 640
        else:
            return 0
    elif len(zs) == 6:
        if sameNumb == 3:
            return 1
        elif sameNumb == 4:
            return 5
        elif sameNumb == 5:
            return 80
        elif sameNumb == 6:
            return 1800
        else:
            return 0
    elif len(zs) == 7:
        if sameNumb == 3:
            return 1
        elif sameNumb == 4:
            return 3
        elif sameNumb == 5:
            return 12
        elif sameNumb == 6:
            return 125
        elif sameNumb == 7:
            return 5000
        else:
            return 0
    elif len(zs) == 8:
        if sameNumb == 4:
            return 2
        elif sameNumb == 5:
            return 7
        elif sameNumb == 6:
            return 60
        elif sameNumb == 7:
            return 675
        elif sameNumb == 8:
            return 25000
        else:
            return 0
    elif len(zs) == 9:
        if sameNumb == 4:
            return 1
        elif sameNumb == 5:
            return 5
        elif sameNumb == 6:
            return 20
        elif sameNumb == 7:
            return 210
        elif sameNumb == 8:
            return 2500
        elif sameNumb == 9:
            return 100000
        else:
            return 0
    elif len(zs) == 10:
        if sameNumb == 4:
            return 1
        elif sameNumb == 5:
            return 2
        elif sameNumb == 6:
            return 6
        elif sameNumb == 7:
            return 50
        elif sameNumb == 8:
            return 580
        elif sameNumb == 9:
            return 10000
        elif sameNumb == 10:
            return 1000000
        else:
            return 0
game = keno()
x = input("Enter the numbers you want to play: ")
slap = slap(x)
for i in range(len(xs)):
    for j in range(len(zs)):
        if zs[j] == xs[i]:
            sameNumb += 1
print("${0}".format(winnings()))
