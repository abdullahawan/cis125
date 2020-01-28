# Muhammad Awan
# Learning functions


def askNumber():
    num = int(input('Enter a number: '))
    return num


def addNumbers(num1, num2):
    result = num1 + num2
    return result


def printResult(result):
    print(result)


# main()

num1 = askNumber()
num2 = askNumber()

result = addNumbers(num1, num2)
printResult(result)
