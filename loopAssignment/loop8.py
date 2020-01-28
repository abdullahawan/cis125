# Muhammad Awan
# Loop program #8


total = 0

for x in range(7):
    x += 1
    userBug = int(input('Enter a bugs collected for day %d: ' % x))
    total += userBug

print('Total of', total, 'bugs collected')

