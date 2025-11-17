#input: [11,22,33,44,55,66]
#output: [22,11,44,33,66,55]

#WAP to replace adjacent numbers.

L = [11,22,33,44,55,66]

for ip in range(0,len(L),2):
    L[ip],L[ip+1]=L[ip+1],L[ip]

print(L)
    