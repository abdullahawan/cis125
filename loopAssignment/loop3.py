# Muhammad Awan
# Loop program #3

def usernum():
    userNum = int(input('Enter an even number: '))
    if userNum % 2 == 0:
        print('Congratulations!')
    else:
        print('You have entered an invalid number, please try again')
        return True


# main()

userNum = usernum()

while userNum:
    userNum = usernum()
