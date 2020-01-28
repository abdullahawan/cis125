# Muhammad Awan
# Loop program #7


def userNums():
    global sum
    num1 = float(input('Enter number 1: '))
    num2 = float(input('Enter number 2: '))

    sum += num1 + num2


def tryAgain():
    ask = input('Would you like to enter another number: (y/n) ')
    if ask.lower() == 'y':
        return True
    return False


# main()
sum = 0

ask = True

while ask:
    userNums()
    ask = tryAgain()

print('\nSum is:', sum)
