#WAP to find the max number among 5 numbers

num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
num3 = int(input('Enter 3rd Number: '))
num4 = int(input('Enter 4th Number: '))
num5 = int(input('Enter 5th number: '))
if num1 > num2:
    if num1>num3:
        if num1>num4:
            if num1>num5:
                print(f'{num1} is max')
            else:
                print(f'{num5} is max')
        else:
            if num4>num5:
                print(f'{num4} is max')
            else:
                print(f'{num5} is max')
    else:
        if num3>num4:
            if num3>num5:
                print(f'{num3} is max')
            else:
                print(f'{num5} is max')
        else:
            if num4>num5:
                print(f'{num4} is max')
            else:
                print(f'{num5} is max')
else:
    if num2>num3:
        if num2>num4:
            if num2>num5:
                print(f'{num2} is max')
            else:
                print(f'{num5} is max')
        else:
            if num4>num5:
                print(f'{num4} is max')
            else:
                print(f'{num5} is max')
    else:
        if num3>num4:
            if num3>num5:
                print(f'{num3} is max')
            else:
                print(f'{num5} is max')
        else:
            if num4>num5:
                print(f'{num4} is max')
            else:
                print(f'{num5} is max')