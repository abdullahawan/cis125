# Muhammad Awan
# Paint Estimating Program 2/6/19
# CIS 125

userSquareFeet = float(input('Please enter square feet of the area: '))
paintPrice = float(input('Enter price of paint: '))

squareFeet = userSquareFeet / 115

laborCharge = 20.00
hoursOfLabor = squareFeet * 8
numberOfGallons = int(squareFeet * 1)


gallons = int(squareFeet * paintPrice)
labor = hoursOfLabor * laborCharge

totalCost = gallons + labor

print("\nSquare Feet Entered \t Price of paint \t Gallons of paint \t Cost of Paint")
print("---------------   \t    --------------   \t ---------------   \t  -------------")
print("    %.2f          \t    %.2f         \t       %d       \t         %.2f"
      % (userSquareFeet, paintPrice, numberOfGallons, gallons))
print("\nPrice of labor     \t     Hours      \t   Total Cost")
print("--------------- \t -------------- \t ------------- ")
print("    %.2f       \t     %.2f      \t    %.2f"
      % (laborCharge, hoursOfLabor, totalCost))


