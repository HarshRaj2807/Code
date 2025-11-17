#WAP to find sum of even digits present in a given string

str = input('Enter string: ')                             #taking input from user. example: 'abc1234def5678ghij'
summ = 0                                                  #initializing sum variable as 0 because there might not be any even digit
for ele in str:                                           #iterating through each character in the string
   # if ele.isdigit() and int(ele) % 2==0:         
    if ele in '2468':                                     #checking if the character is an even digit
        summ+=int(ele)                                    #adding the even digit to the sum variable

print(summ)                                               #printing the sum of even digits

#1st iteration: str = 'abc1234def5678ghij', ele = 'a', ele.isdigit() = False, summ = 0
#2nd iteration: str = 'abc1234def5678ghij', ele = 'b', ele.isdigit() = False, summ = 0
#3rd iteration: str = 'abc1234def5678ghij', ele = 'c', ele.isdigit() = False, summ = 0
#4th iteration: str = 'abc1234def5678ghij', ele = '1', ele.isdigit() = True, ele in '2468' = False, summ = 0
#5th iteration: str = 'abc1234def5678ghij', ele = '2', ele.isdigit() = True, ele in '2468' = True, summ = 0 + 2 = 2
#6th iteration: str = 'abc1234def5678ghij', ele = '3', ele.isdigit() = True, ele in '2468' = False, summ = 2
#7th iteration: str = 'abc1234def5678ghij', ele = '4', ele.isdigit() = True, ele in '2468' = True, summ = 2 + 4 = 6
#8th iteration: str = 'abc1234def5678ghij', ele = 'd', ele.isdigit() = False, summ = 6
#9th iteration: str = 'abc1234def5678ghij', ele = 'e', ele.isdigit() = False, summ = 6
#10th iteration: str = 'abc1234def5678ghij', ele = 'f', ele.isdigit() = False, summ = 6
#11th iteration: str = 'abc1234def5678ghij', ele = '5', ele.isdigit() = True, ele in '2468' = False, summ = 6
#12th iteration: str = 'abc1234def5678ghij', ele = '6', ele.isdigit() = True, ele in '2468' = True, summ = 6 + 6 = 12
#13th iteration: str = 'abc1234def5678ghij', ele = '7', ele.isdigit() = True, ele in '2468' = False, summ = 12
#14th iteration: str = 'abc1234def5678ghij', ele = '8', ele.isdigit() = True, ele in '2468' = True, summ = 12 + 8 = 20
#15th iteration: str = 'abc1234def5678ghij', ele = 'g', ele.isdigit() = False, summ = 20
#16th iteration: str = 'abc1234def5678ghij', ele = 'h', ele.isdigit() = False, summ = 20
#17th iteration: str = 'abc1234def5678ghij', ele = 'i', ele.isdigit() = False, summ = 20
#18th iteration: str = 'abc1234def5678ghij', ele = 'j', ele.isdigit() = False, summ = 20
#Final output: 20