#WAP to print how many given substring is present in a given string.
#                                 or
#Implement count method logic.

str1 = input("Enter String : ")            #we take input string from user. example "Harsh"
str2 = input("Enter substring : ")         #we take input substring from user. example "a"
count = 0                                  #we initialize count to 0 because there might be no substring.

for ele in str1:                           #in the for loop we iterate through each element in the string.
    if ele==str2:                          #we check if the 1st element (H) is equal to the substring (a)
                                           #we do not increment count as they are not equal and move to the next element.  
        count+=1                           #we increment count by 1 as they are equal and move to the next element (r) 
                                           #we do not increment count as they are not equal and move to the next element (s)

print(count, 'substrings in the string')   #we print the count of substring in the string.