#WAP to print how many vowels are present in a given string.

str = input("Enter String : ")                                 #we take input string from user. example "Harsh"
vowels = 'aeiou'                                               #we define vowels in a string.
count = 0                                                      #we initialize count to 0 because there might be no vowels.
for ele in str:                                                #in the for loop we iterate through each element in the string.
    if ele.lower() in vowels:                                  #we convert the element to lowercase and check if it is in the vowels string.
        count+=1                                               #we check if the first element (H) is a vowel and it is not so we do not increment count.
                                                               #then we check the next element (a) and it is a vowel so we increment
                                                               #then we check the next element (r) and it is not a vowel so we do not increment count.
                                                               # then we check the next element (s) and it is not a vowel so we do not increment count.                                                               
print(count)                                                   #we print the count of vowels in the string.
                                                               #or we can use the built-in count() method to get the count of vowels in the string.
                                                               #print('Number of vowels in the string is', str.lower().count('a') + str