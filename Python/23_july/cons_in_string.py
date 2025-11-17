#WAP to print how many consonents are present in a given string.

str = input("Enter String : ")    #we take input string from user. example "Harsh"
vowels = 'aeiou'                  #we define vowels in a string.
count = 0                         #we initialize count to 0 because there might be no consonants.
for ele in str:                   #in for loop we iterate through each element in the string.
                                  #we check if the element is an alphabet, is converted into lowercase and not a vowel 
    if ele.isalpha() and ele.lower() not in vowels :
        count+=1                   #we check if the first elemnt (H) is a consonant and increment count by 1.
                                   #then we check the next element (a) and it is not a consonant so we do not increment count.
                                   #then we check the next element (r) and it is a consonant so we increment count by 1.
                                   #then we check the next element (s) and it is a consonant so we increment count by 1.                

print(count)                       #we print the count of consonants in the string.