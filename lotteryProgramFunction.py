# Muhammad Awan
# Lottery program

import random


def tryAgain():
    again = input('\nWould you like to try again? (y/n): ')
    if again.lower() == 'y':
        runProgram()
    elif again.lower() == 'n':
        print('Ending program...')
    else:
        print('The input you entered is invalid, try again.')
        tryAgain()

def randomNum():
    global randomList
    randomNum1 = random.randrange(0, 10)
    randomNum2 = random.randrange(0, 10)
    randomNum3 = random.randrange(0, 10)
    randomList = [randomNum1, randomNum2, randomNum3]
    print(randomList)


def askUserNumber():
    global userList
    print('----------------------------------------------')
    userNum1 = int(input('\nEnter number 1:'))
    userNum2 = int(input('Enter number 2:'))
    userNum3 = int(input('Enter number 3:'))
    userList = [userNum1, userNum2, userNum3]


def checkNumbers():
    i = 0
    for num1 in userList:
        for num2 in randomList:
            if num1 == num2:
                i += 1

    if i == 1:
        print('You won $10')
    elif i == 2:
        print('You won $1,000')
    elif userList == randomList:
        print('You won $100,000')
    elif set(userList) == set(randomList):
        print('You won $10,000')
    else:
        print('Better luck next time')

    # if userList == randomList:
    #     print('You won!')
    #     print('You\'re winning number is:', randomList)
    # else:
    #     print('Sorry you lost')
    #     print('You\'re number was:', userList)
    #     print('The winning number was:', randomList)


def runProgram():
    randomNum()
    askUserNumber()
    checkNumbers()
    tryAgain()

# main()

runProgram()


