# Muhammad Awan
# Decision Programming Assignment


# #1
print('\n--------------------------------------------------')
print('Question 1')
num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))
if num1 > num2:
    print('The bigger number is: %d' % num1)
else:
    print('The bigger number is: %d' % num2)


# #2
print('\n--------------------------------------------------')
print('Question 2')
age = int(input('Enter your age: '))
major = input('Enter your major: ')
gpa = float(input('Enter your GPA: '))

if major.lower() == "science" and age >= 20 and gpa > 3.50:
    print('Setup a meeting with this student!')
else:
    print('Don\'t set up a meeting with this student!')


# #3
print('\n--------------------------------------------------')
print('Question 3')
grade = int(input('Enter the student\'s test grade: '))

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('E')

# #4
print('\n--------------------------------------------------')
print('Question 4')
num = int(input('Enter an integer between 1 and 20: '))

if num == 1:
    print('%dst' % num)
elif num == 2:
    print('%dnd' % num)
elif num == 3:
    print('%drd' % num)
elif num >= 4 and num <= 20:
    print('%dth' % num)
else:
    print('You didn\'t enter a number between 1 and 20')

# #5
print('\n--------------------------------------------------')
print('Question 5')
test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))
grade = (test1 + test2 + test3) / 3
print('You\'re percentage is: %.2f' % grade)
print('You\'re score is: ')
if grade <= 100 and grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('E')



