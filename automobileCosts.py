# Muhammad Awan
# Automobile Costs


def askLoanPayment():
    loanPayment = float(input('Enter monthly loan payment: $'))
    return loanPayment


def askInsurance():
    insurance = float(input('Enter monthly insurance payment: $'))
    return insurance


def askGas():
    gas = float(input('Enter monthly gas payment: $'))
    return gas


def askOil():
    oil = float(input('Enter oil payment: $'))
    return oil


def askTires():
    tires = float(input('Enter tires payment for 4 tires: $'))
    return tires


def askMaintenance():
    maintenance = float(input('Enter maintenance payment: $'))
    return maintenance


def totalMonthlyCosts(loan, insurance, gas, oil, tires, maintenance):
    total = loan + insurance + gas + oil + tires + maintenance
    return total


def totalAnnualCosts(monthlyCost):
    annualCost = monthlyCost * 12
    return annualCost


def displayInfo(monthlyCost, annualCost):
    print('\nMonthly Cost \t Annual Cost')
    print('------------ \t -----------')
    print('  $%.2f  \t\t   $%.2f' % (monthlyCost, annualCost))


# main()

loanPayment = askLoanPayment()
insurance = askInsurance()
gas = askGas()
oil = askOil()
tires = askTires()
maintenance = askMaintenance()

monthlyCost = totalMonthlyCosts(loanPayment, insurance, gas, oil, tires, maintenance)
annualCost = totalAnnualCosts(monthlyCost)

displayInfo(monthlyCost, annualCost)
