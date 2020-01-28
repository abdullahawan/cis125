# Muhammad Awan
# Introduction to loops in Python

x = 10

while x >= 1:
    print(x)
    x -= 1

print('----')
for x in range(5):
    print(x)

print('----')
for x in range(1, 5):
    print(x)

print('----')
for x in range(2, 11, 2):
    print(x)


# Lists
print('----')
cars = ['BMW', 'Porsche', 'Tesla', 'Chevelle']

for car in cars:
    print(car)

print('----')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October',
          'November', 'December']

userMonth = input('Please enter a month: (e.g January) ')
if userMonth in months:
    print(userMonth, 'found!')
else:
    print(userMonth, 'not found!')

userMonth = int(input('Enter month, e.g 10: '))
for month in months:
    if userMonth - 1 == months.index(month):
        print(month, 'found')


print('----')
favCar = input('Enter you favorite car:  ')
if favCar in cars:
    print(favCar, 'Found')
else:
    print(favCar, 'Not found')
