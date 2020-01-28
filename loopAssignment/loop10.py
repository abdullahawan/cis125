# Muhammad Awan
# Loop Assignment #10

tuition = 6000.00
tuitionRaised = 0.02

for x in range(5):
    tuition = (tuition * tuitionRaised) + tuition
    print('Tuition for a semester in year', x + 1, 'is %.2f' % tuition)
