#WAP to reverse a given sting without using slicing

#with negative indexing
S=input('Enter string: ')
new=''
for ip in range(-1,-(len(S)+1),-1):
    new+=S[ip]

#with positive indexing
'''
S=input('Enter string: ')
new=''
for ip in range((len(S)-1),-1,-1):
    new+=S[ip]
'''


#by using elements 
'''
S=input('Enter string: ')
new=''
for ele in S:
    new= ele + new
'''