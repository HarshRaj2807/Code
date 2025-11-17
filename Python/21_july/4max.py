#WAP to find the max number among 4 numbers

num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
num3 = int(input('Enter 3rd Number: '))
num4 = int(input('Enter 4th Number: '))

if num1 > num2:
    if num1>num3:
        if num1>num4:
            print(f'{num1} is max')
        else:
            print(f'{num4} is max')
    else:
        if num3>num4:
            print(f'{num3} is max')
        else:
            print(f'{num4} is max')
else:
    if num2>num3:
        if num2>num4:
            print(f'{num2} is max')
        else:
            print(f'{num4} is max')
    else:
        if num3>num4:
            print(f'{num3} is max')
        else:
            print(f'{num4} is max')