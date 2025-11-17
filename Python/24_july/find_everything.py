#WAP to find how many special characters, alphabets, digits are there in a string.

str = input("Enter String : ")                         #we take input string from user. example "Harsh123!@#"

countofdigit = 0                                       #we initialize countofdigit to 0 because there might be no digits.
countofalpha = 0                                       #we initialize countofalpha to 0 because there might be no alphabets.
countofspecial = 0                                     #we initialize countofspecial to 0 because there might be no special characters.

for ele in str:                                        #in the for loop we iterate through each element in the string. 
    if ele.isalpha():                                  #if the 1st element (H) is an alphabet then we increase the countofalpha by 1 and move to next element.
        countofalpha+=1                                #we increase the countofalpha by 1 in every iteration if the element is an alphabet.

    elif ele.isdigit() :                               #if any element is not an alphabet then we check if it is a digit or not.   
        countofdigit+=1                                #like when we reach 6th element (1) which is not an alphabet, so we check if it's a digit or not.
                                                       #if it is a digit then we increase the countofdigit by 1 and move to next element.
    else:                                              #if the element is neither an alphabet nor a digit then it is definately a special character.
        countofspecial+=1                              #we increase the countofspecial by 1 and move to next element.       

print(countofalpha,'Alphabets')                        #we print the count of alphabets, digits and special characters.
print(countofdigit,'Digits')
print(countofspecial,'Special Characters')