# Muhammad Awan

dearbornCounter = 0

stillPeople = input('Are there people to ask? (y/n) ')

while stillPeople.lower() == 'y':
    dearborn = input('Do you live in Dearborn? (y/n) ')
    
    if dearborn.lower() == 'y':
        dearbornCounter += 1

    stillPeople = input('Are there people to ask? (y/n) ')

print('\nTotal people living in Dearborn: ', dearbornCounter)
