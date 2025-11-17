#WAP to print the given number if number is even or odd.

#Method 1
n= (int(input("Enter number:")))
if n % 2==0:
    print('given number is Even')
else:
    print('given number is Odd')

#Method 2
if n % 2!=0:
    print('given number is Odd')
else:
    print('given number is Even')