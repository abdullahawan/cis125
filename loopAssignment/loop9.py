# Muhammad Awan
# Loop program #9


# main()
budgetLength = int(input('Enter total number of items to budget: '))
budgetAmount = float(input('Enter total budget: $'))
i = 1
sum = 0

while i <= budgetLength:
    budget = float(input('Enter budget for item %d: ' % i))

    sum += budget
    i += 1


print('Total budget for month is $%.2f' % budgetAmount)
difference = budgetAmount - sum
print('\nThe difference is $%.2f' % difference)
