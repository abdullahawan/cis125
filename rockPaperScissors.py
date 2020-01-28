# Muhammad Awan
# Rock Paper Scissors game

import random
import time


def displayChoices():
    print('--------------------------------')
    print('Welcome to Rock, Paper, Scissors')
    print('Enter the number of your choice')
    print('Rock: 1 \nPaper: 2 \nScissors: 3')


def getUserChoice():
    userChoice = int(input('\nPlease enter your choice (1, 2, or 3): '))
    return userChoice


def checkChoice(userChoice):
    if userChoice in choices:
        return True
    return False


def checkWin(userChoice):
    global userWins, computerWins, tieGame

    rockWins = [1, 3]
    paperWins = [2, 1]
    scissorWins = [3, 2]

    if userChoice == choiceChosen[1]:
        print('Tie game!')
        tieGame += 1
    elif set(choiceChosen) == set(rockWins):
        if userChoice == rockWins[0]:
            print('User wins! Rock beats Scissors!')
            userWins += 1
        else:
            print('Computer wins! Rock beats Scissors')
            computerWins += 1
    elif set(choiceChosen) == set(rockWins):
        if userChoice == paperWins[0]:
            print('User wins! Paper beats Rock!')
            userWins += 1
        else:
            print('Computer wins! Paper beats Rock!')
            computerWins += 1
    else:
        if userChoice == scissorWins[0]:
            print('User wins! Scissor beats Paper!')
            userWins += 1
        else:
            print('Computer wins! Scissor beats Paper!')
            computerWins += 1


def playAgain():
    global gameOver

    choice = input('Would you like to play again? (y/n) ')
    if choice.lower() == 'n':
        gameOver = True
    elif choice.lower() == 'y':
        print('Playing again...')
    else:
        print('Invalid input, choose again')
        playAgain()


# main()
choices = [1, 2, 3]

userWins = 0
computerWins = 0
tieGame = 0

gameOver = False

while not gameOver:
    computerChoice = random.choice(choices)
    displayChoices()

    userChoice = getUserChoice()

    validation = checkChoice(userChoice)

    if validation:
        print('You chose:', userChoice)
        print('Computer chose:', computerChoice)

        choiceChosen = [userChoice, computerChoice]

        checkWin(userChoice)
        playAgain()
    else:
        print('The number you entered was invalid')
        time.sleep(1)


print('\n--------------------------------')
print('User won', userWins, 'time(s)')
print('Computer won', computerWins, 'time(s)')
print('You had', tieGame, 'tie game(s)')

