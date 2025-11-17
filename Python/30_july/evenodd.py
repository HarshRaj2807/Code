#input: [11,22,33,10,222]
#output: ['odd','even','odd','even','even']

#wap to replace all numbers with either even or odd based on their value.


#modivfying existing list
'''
L = eval(input('Enter list: '))

for ele in L:
    if ele%2==0:
        print('even')
    else:
        print('odd')
print(L)
'''
'''
L = eval(input('Enter list: '))

for ip in range(len(L)):
    if L[ip]%2==0:
        L[ip]='even'
    else:
        L[ip]='odd'
print(L)
'''


#without modifying existing list
L = eval(input('Enter list: '))
new = []

for ip in range(len(L)):
    if L[ip]%2==0:
        new.append('even')
    else:
        new.append('odd')
print(new)