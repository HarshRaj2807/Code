#WAP to print even numbers in a given range.

a = int(input('enter starting range: '))
b = int(input('enter ending range: '))
c = int(input('enter updation value (-2 or 2): '))


if a%2==1:
    a+=1

a = int(input())
summ=0
for n in range(1,a+1):
    summ+=n
print('sum of all numbers is :', summ)
if c==2:
    for n in range(a,b+1,c):
        print(n)
else:
    for n in range(a,b-1,c):
        print(n)