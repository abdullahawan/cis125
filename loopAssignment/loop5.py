# Muhammad Awan
# Loop program #5


def commission():
    sales = float(input('Enter Sale Amount: $'))

    if sales == int(-1):
        return False

    comp = sales * .12
    print('Commission is $%.2f' % comp)
    return True


# main()

sale = commission()

while sale:
    sale = commission()
