#WAP to print factorial of a given number.

a = int(input())
fact=1
for n in range(1,a+1):
    fact*=n
print("factoral of",a,"is :", fact)