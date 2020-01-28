# Muhammad Awan
# Workshop Calculator


def display():
    print('\nWhich number workshop would you like to attend?')
    print('1    Handling Stress')
    print('2    Time Management')
    print('3    Supervision Skills')
    print('4    Negotiation')
    print('5    How to Interview')


def getWorkshop():
    ws = int(input('Please enter the number --> '))
    return ws


def validateWorkshop(ws):
    if ws in workshop:
        return True
    return False


def getDays(ws):
    days = workshopDaysAndFees[ws][0]
    return days


def getRegistrationFees(ws):
    fees = workshopDaysAndFees[ws][1]
    return fees


def displayInitialChoices(ws, days, regFee):
    print(f'\nYou have chosen to attend the {ws} workshop')
    print(f'Number of days: {days}')
    print(f'Registration Fee:  ${regFee:.2f}')


def displayLocations():
    print('\nPlease choose a location')
    for lc in locations:
        print(lc)


def getLocation():
    print('\n[!] Location is case-sensitive, please enter it exactly as seen')
    lc = input('Please choose a location --> ')
    return lc


def validateLocation(lc):
    if lc in locations:
        return True
    return False


def calculateAndDisplayCosts(costs, days, fees):
    total = fees + (days * costs)

    print(f'\nRegistration Fees : ${fees:.2f}')
    print(f'Lodging Costs : ${(days * costs):.2f}')
    print(f'Total Workshop Cost: ${total:.2f}')


def confirmRsvp():
    confirm = input('\nWould you like to register for this workshop? (yes/no) ')
    if confirm.lower().startswith('y'):
        return True
    elif confirm.lower().startswith('n'):
        return False
    else:
        return confirmRsvp()


def displayTotal(ws, lc, days, cost, fee):
    total = (days * cost) + fee
    print(f'\nYou have registered for the {ws} workshop in {lc}')
    print(f'    Registration Fees : ${fee:.2f}')
    print(f'    Lodging Costs : ${(days * cost):.2f}')
    print(f'    Total Workshop Cost : ${total:.2f}')
    print('Please enjoy your workshop!')


def main():
    display()

    # get and validate workshop
    ws = getWorkshop()

    while validateWorkshop(ws) is False:
        ws = getWorkshop()

    # get workshop days, fees, and display initial choices
    ws = workshop[ws]
    days = getDays(ws)
    fees = getRegistrationFees(ws)
    displayInitialChoices(ws, days, fees)

    # display and get location, validate
    displayLocations()
    lc = getLocation()

    while validateLocation(lc) is False:
        lc = getLocation()

    # Calculates Locations costs + fees, prints total
    lcCosts = locations[lc]
    displayInitialChoices(ws, days, fees)
    calculateAndDisplayCosts(lcCosts, days, fees)

    # confirms if they want to join chosen workshop
    confirm = confirmRsvp()
    if confirm:
        displayTotal(ws, lc, days, lcCosts, fees)
        return True
    else:
        print('Sorry to see you go!')
        return False


# setting dicts, lists, and calling main()
workshop = {1: 'Handling Stress', 2: 'Time Management', 3: 'Supervision Skills', 4: 'Negotiation',
            5: 'How to Interview'}

workshopDaysAndFees = {'Handling Stress': [3, 1000.00], 'Time Management': [3, 800.00],
                       'Supervision Skills': [3, 1500.00], 'Negotiation': [5, 1300.00], 'How to Interview': [1, 500.00]}

locations = {'Austin': 150.00, 'Chicago': 225.00, 'Dallas': 175.00, 'Detroit': 150.00, 'Orlando': 300.00,
             'Phoenix': 175.00}

if __name__ == "__main__":
    confirm = main()
    while confirm is False:
        confirm = main()
