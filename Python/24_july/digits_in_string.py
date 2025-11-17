#WAP to print how many digits are present in a given string.

str = input("Enter String : ")                                  #we take input string from user. example "Harsh123"

count = 0                                                       #we initialize count to 0 because there might be no digits.
for ele in str:                                                 #in the for loop we iterate through each element in the string.
    if ele.isdigit(): # (without built in method this can be used)      if ele>='0' and ele<='9':
        count+=1                                                #we check if the first element (H) is a digit and it is not so we do not increment count.
                                                                #then we check the next element (a) and it is not a digit so we do not increment count.
                                                                #then we check the next element (r) and it is not a digit so we do not increment count.
                                                                #similarly check the next elements and if it is not a digit so we do not increment count.
                                                                #when we check the element (1) and it is a digit so we increment count by 1.
                                                                #then we check the next element (2) and it is a digit so we increment count by 1.

print(count)                                                    #we print the count of digits in the string.
                                                                #or we can use the built-in count() method to get the count of digits in the string.
                                                                #print('Number of digits in the string is', sum(1 for ele in str if ele.isdigit()))