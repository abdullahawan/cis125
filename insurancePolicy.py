# Muhammad Awan
# Calculates policy amount based on the type of policy

from termcolor import colored

insuranceRates = [250.00, 125.00, 75.00]
insurancePolicies = [1, 2, 3, 4, 5, 6, 7]
insurancePolicy = ['Health Insurance', 'Auto Insurance', 'Life Insurance', 'Health and Auto',
                   'Auto and Life', 'Health and Life', 'Health, Auto and Life (all three)']


def askAgain():
    ask = input('Would you like to choose another policy? (y/n)')
    if ask.lower() == 'y':
        policyInfo = askPolicyType()
        displayPolicy(policyInfo)
        askAgain()
    elif ask.lower() == 'n':
        print('Ending program...')
    else:
        print(colored('Sorry, unable to recognize input. Try again.', 'red', attrs=['reverse']))
        askAgain()


def userPolicyAmount(userPolicy):
    # Sets the policy amount
    if userPolicy <= 3:
        policyAmount = insuranceRates[userPolicy - 1]
        return policyAmount
    elif userPolicy <= 5:
        policyAmount = insuranceRates[userPolicy - 4] + insuranceRates[userPolicy - 3]
        return policyAmount
    elif userPolicy == 6:
        policyAmount = insuranceRates[0] + insuranceRates[2]
        return policyAmount
    else:
        policyAmount = insuranceRates[0] + insuranceRates[1] + insuranceRates[2]
        return policyAmount


def getUserPolicy(userPolicy):
    chosenPolicy = ''
    userPolicy = userPolicy - 1
    for policy in insurancePolicy:
        if insurancePolicy.index(policy) == userPolicy:
            chosenPolicy = policy

    return chosenPolicy


def displayPolicy(policyInfo):
    userPolicy = policyInfo[1]
    policyAmount = policyInfo[3]
    discountApplied = policyInfo[4][1] * 100
    monthlyPremium = policyInfo[4][0]
    chosenPolicy = policyInfo[2]

    print('\nInsurance Policy Chosen \t Policy Amount \t Discount Applied (%) \t Total Monthly Premium')
    print('----------------------- \t ------------- \t -------------------- \t ---------------------')
    print('%23d   \t $%12.2f \t  %19.2f \t $%20.2f' %
          (userPolicy, policyAmount, discountApplied, monthlyPremium))

    print('\nYour policy is:', chosenPolicy)


def validatePolicyType(userPolicy):
    if userPolicy in insurancePolicies:
        print('The policy you entered is valid.')
        print('Getting policy information and discounts...')
        return True
    else:
        print(colored('The policy number you entered is invalid, try again.', 'red', attrs=['reverse']))
        return False


def checkDiscountAndMonthly(userPolicy, policyAmount):
    twoDiscount = 0.1
    threeDiscount = 0.2

    if userPolicy > 3 and userPolicy < 7:
        monthlyPremium = policyAmount - (policyAmount * twoDiscount)
        return monthlyPremium, twoDiscount
    elif userPolicy == 7:
        monthlyPremium = policyAmount - (policyAmount * threeDiscount)
        return monthlyPremium, threeDiscount
    else:
        monthlyPremium = policyAmount
        return monthlyPremium, 0


def askPolicyType():
    print('\nPolicy 1: Health Insurance')
    print('Policy 2: Auto Insurance')
    print('Policy 3: Life')
    print('Policy 4: Health and Auto')
    print('Policy 5: Auto and Life')
    print('Policy 6: Health and Life')
    print('Policy 7: Health, Auto, and Life (all three)')
    userPolicy = int(input('\nPlease choose a policy type from above (1-7): '))

    # Validates Policy
    validPolicy = validatePolicyType(userPolicy)

    if validPolicy:
        # Gets insurance policy title
        chosenPolicy = getUserPolicy(userPolicy)

        # Sets policy amount variable
        policyAmount = userPolicyAmount(userPolicy)

        # Checks discount and sets variable
        discountAndMonthly = checkDiscountAndMonthly(userPolicy, policyAmount)

        # returns user policy, amount, discounts, and monthly premiums
        return validPolicy, userPolicy, chosenPolicy, policyAmount, discountAndMonthly
    else:
        return askPolicyType()




# main()
policyInfo = askPolicyType()
if policyInfo[0]:
    displayPolicy(policyInfo)
    askAgain()
