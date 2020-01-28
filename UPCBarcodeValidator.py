# Muhammad Awan
# This program validates barcode

firstVal = int(input('Enter first value: '))
manCode = list(map(int, input('Enter first five numbers: ')))
prodCode = list(map(int, input('Enter second set of five numbers: ')))
checkDigit = int(input('Enter last value: '))

stepA = manCode[1] + manCode[3]
stepB = prodCode[0] + prodCode[2] + prodCode[4]
stepC = (stepA + stepB) * 3
stepD = manCode[0] + manCode[2] + manCode[4]
stepE = prodCode[1] + prodCode[3]
stepF = (stepD + stepE) + stepC
stepG = stepF % 10
stepH = 10 - stepG

if stepH == checkDigit:
    print('Valid UPC Barcode:\n', firstVal, manCode, prodCode, checkDigit)
else:
    print('UPC Barcode is not valid!\n', firstVal, manCode, prodCode, checkDigit)