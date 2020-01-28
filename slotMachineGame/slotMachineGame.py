# Muhammad Awan
# Slot Machine Game

import random
import time


def display():
    print('Welcome to the SLOT MACHINE')
    print('Each try is $1')
    print('Your choices are: x, y, z, $')


def getTurns():
    turns = int(input('Enter the number of turns to play. (Each turn is $1) '))
    return turns


def getMachineChoices():
    choice1 = random.choice(choices)
    choice2 = random.choice(choices)
    choice3 = random.choice(choices)

    answers.append(choice1)
    answers.append(choice2)
    answers.append(choice3)


def getWinnings():
    x, y, z, w = 0, 0, 0, 0
    winnings = 0

    global totalWinnings

    for answer in answers:
        if answer is 'x':
            x += 1
        elif answer is 'y':
            y += 1
        elif answer is 'z':
            z += 1
        else:
            w += 1

    if x == 3:
        winnings = 250
    elif y == 3:
        winnings = 150
    elif z == 3:
        winnings = 50
    elif w == 3:
        winnings = 1000
    elif x == 2:
        winnings = 50
    elif y == 2:
        winnings = 25

    if w == 2:
        winnings += 750
    elif w == 1:
        winnings += 500

    totalWinnings += winnings
    print('The Combination was', answers)
    print('You won a total of $%d' % winnings)


def playAgain():
    ask = input('Would you like to play again? (y/n) ')

    if ask.lower() == 'y':
        return True
    elif ask.lower() == 'n':
        return False
    else:
        return playAgain()


# main()
totalWinnings = 0
choices = ['x', 'y', 'z', '$']
answers = []

display()
turns = getTurns()

i = 1

while i <= turns:
    getMachineChoices()
    time.sleep(1)
    print('-----------------------------------------------------')
    getWinnings()

    i += 1
    answers = []

    if i > turns:
        print('-----------------------------------------------------')
        print('Your total winnings are $%d' % totalWinnings)
        print('-----------------------------------------------------')
        ask = playAgain()
        if ask:
            i = 1
            answers = []
            display()
            turns = getTurns()
