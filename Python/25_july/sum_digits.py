#WAP to find sum of digits in present in a given string.

str = input('Enter string: ')                              #taking input from user. example: 'abc1234def5678ghij'
summ = 0                                                   #initializing sum variable as 0 because there might not be any digit
for ele in str:                                            #iterating through each character in the string
    if ele.isdigit():                                      #checking if the character is a digit
        summ+=int(ele)                                     #adding the digit to the sum variable

print(summ)                                                #printing the sum of digits


#1st iteration: str = 'abc1234def5678ghij', ele = 'a', ele.isdigit() = False, summ = 0
#2nd iteration: str = 'abc1234def5678ghij', ele = 'b', ele.isdigit() = False, summ = 0
#3rd iteration: str = 'abc1234def5678ghij', ele = 'c', ele.isdigit() = False, summ = 0
#4th iteration: str = 'abc1234def5678ghij', ele = '1', ele.isdigit() = True, summ = 0 + 1 = 1
#5th iteration: str = 'abc1234def5678ghij', ele = '2', ele.isdigit() = True, summ = 1 + 2 = 3
#6th iteration: str = 'abc1234def5678ghij', ele = '3', ele.isdigit() = True, summ = 3 + 3 = 6
#7th iteration: str = 'abc1234def5678ghij', ele = '4', ele.isdigit() = True, summ = 6 + 4 = 10
#8th iteration: str = 'abc1234def5678ghij', ele = 'd', ele.isdigit() = False, summ = 10
#9th iteration: str = 'abc1234def5678ghij', ele = 'e', ele.isdigit() = False, summ = 10
#10th iteration: str = 'abc1234def5678ghij', ele = 'f', ele.isdigit() = False, summ = 10
#11th iteration: str = 'abc1234def5678ghij', ele = '5', ele.isdigit() = True, summ = 10 + 5 = 15
#12th iteration: str = 'abc1234def5678ghij', ele = '6', ele.isdigit() = True, summ = 15 + 6 = 21
#13th iteration: str = 'abc1234def5678ghij', ele = '7', ele.isdigit() = True, summ = 21 + 7 = 28
#14th iteration: str = 'abc1234def5678ghij', ele = '8', ele.isdigit() = True, summ = 28 + 8 = 36
#15th iteration: str = 'abc1234def5678ghij', ele = 'g', ele.isdigit() = False, summ = 36
#16th iteration: str = 'abc1234def5678ghij', ele = 'h', ele.isdigit() = False, summ = 36
#17th iteration: str = 'abc1234def5678ghij', ele = 'i', ele.isdigit() = False, summ = 36
#18th iteration: str = 'abc1234def5678ghij', ele = 'j', ele.isdigit() = False, summ = 36
#Final output: 3