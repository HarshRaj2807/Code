#WAP to print if given string is palindrome or not.

str = str(input("Enter string: "))
if str == str[::-1]:
    print(f'{str} is palindrome')
else:
    print(f'{str} is not a palindrome')