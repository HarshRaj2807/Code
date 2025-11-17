#WAP to find max number among 3 numbers using nested if.

num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
num3 = int(input('Enter 3rd Number: '))

if num1 > num2:
    if num1>num3:
        print(f'{num1} is highest')
    else:
        print(f'{num3} is highest')
else:
    if num2>num3:
        print(f'{num2} is highest')
    else:
        print(f'{num3} is highest')
