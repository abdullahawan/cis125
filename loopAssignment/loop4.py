# Muhammad Awan
# Loop program #4


def usernum():
    userNum = int(input('Enter a number: '))
    numList.append(userNum)

    if userNum == int(-1):
        return False
    return True


# main()
numList = []

print('Enter any number. Enter -1 to end.')
userNum = usernum()

while userNum:
    userNum = usernum()

print('The largest number is', max(numList))
