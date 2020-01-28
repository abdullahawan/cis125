# Muhammad Awan
# Loop program #2


def usernum():
    global product

    userNum = int(input('Enter a number: '))
    product += userNum * 10


# main()
product = 0

usernum()
while product < 100:
    usernum()
