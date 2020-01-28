# Muhammad Awan
# Program that calculates weight loss

userWeight = int(input('What is your starting weight: '))

i = 0
weightLoss = 4
currentWeight = userWeight

print('Starting weight:', currentWeight, 'pounds')
print('\n Month \t Weight')
print('------ \t ------')
while i < 6:
    i += 1
    userWeight = userWeight - 4
    print('  %i  \t  %d' %(i, userWeight))


month1 = currentWeight - 4
month2 = month1 - 4
month3 = month2 - 4
month4 = month3 - 4
month5 = month4 - 4
month6 = month5 - 4

print('\nStarting weight:', currentWeight, 'pounds')
print('\n Month \t Weight')
print('------ \t ------')
print('   1  \t ', month1)
print('   2  \t ', month2)
print('   3  \t ', month3)
print('   4  \t ', month4)
print('   5  \t ', month5)
print('   6  \t ', month6)

