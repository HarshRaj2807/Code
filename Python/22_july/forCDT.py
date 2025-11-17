#for loop with string
s= input()
for ele in s:
    print(ele)

#for loop with list
L = [11,22,33,'hai',[10,20]]
for ele in L:
    print(ele)

#for loop with tuple
T = 11,22,33,'hai',[10,20]
for ele in T:
    print(ele)

#for loop with set
S = {11,22,33,'hai',(10,20)}
for ele in S:
    print(ele)

#for loop with Dictionary
D = {'name' : 'ashu', 'age' : 6}
for key in D:
    print(key,D[key])

#for loop with Dictionary's itmes method
D = {'name' : 'ashu', 'age' : 6}
for ele in D.items():
    print(ele)                        
#note: this above process will extract enitre element from the given dictionary

#for loop with 2 variables in Dictionary's itmes method
D = {'name' : 'ashu', 'age' : 6}
for key,value in D.items():
    print(key,value)