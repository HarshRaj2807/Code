#WAP to print how many elements are present in a given string
#                          or 
#length method logic
str = input("Enter String : ")                                     #we take input string from user. example "Harsh"

count = 0                                                          #we initialize count to 0 because there might be no elements in the string.
for ele in str:                                                    #in the for loop we iterate through each element in the string.
    count+=1                                                       #we increment count by 1 for each element in the string.
                                                                   #we check the first element (H) and increment count by 1.
                                                                   #then we check the next element (a) and increment count by 1.
                                                                   #then we check the next element (r) and increment count by 1.
                                                                   #then we check the next element (s) and increment count by 1.
                                                                   #then we check the next element (h) and increment count by 1.

print('Number of elements in the string is',count)                 #we print the count of elements in the string.
                                                                   #or we can use the built-in len() function to get the length of the string
                                                                   #print('Number of elements in the string is',len(str))             