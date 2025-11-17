#WAP to print a string if it has vowels as their last characters.

str = input("Enter String: ")

if str[-1].lower in 'aeiou':
    print(str)
else:
    print("String does not end with vowel.")