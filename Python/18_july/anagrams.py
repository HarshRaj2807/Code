#WAP to print of the given strings are anagrams or not.

str1 = (input("Enter 1st String: "))
str2 = (input("Enter 2nd String: "))
if sorted(str1) == sorted(str2):
    print(f'{str1} and {str2} are anagrams')
else:
    print(f'{str1} and {str2} are not anagrams')