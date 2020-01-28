# Muhammad Awan
# Property Taxes program
# 2/13/19

def getPropertyValue():
    property = float(input('Enter value of property: $'))
    return property


def calculateAssessmentValue(propertyValue):
    value = propertyValue * 0.6
    return value


def calculateTaxValue(assessmentValue):
    taxValue = assessmentValue / 100
    taxValue = taxValue * 0.64
    return taxValue


def displayValues(propertyValue, assessmentValue, taxValue):
    print('\nProperty Value \t Assessment Value \t Property Tax')
    print('-------------- \t ---------------- \t ------------')
    print('$%13.2f \t $%15.2f  \t $%11.2f' % (propertyValue, assessmentValue, taxValue))


# main()

userProperty = getPropertyValue()

assessmentValue = calculateAssessmentValue(userProperty)
taxValue = calculateTaxValue(assessmentValue)

displayValues(userProperty, assessmentValue, taxValue)

