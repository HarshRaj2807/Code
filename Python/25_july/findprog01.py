# input 1 = [11,20,'hai12','25',['bye',40],[10]]
# output = 56

#input 2 = [2,5,6,'78',[50],'hu8']
#output = 91

#find the sum of integers and string of integers in a given list

list = eval(input('Enter list:'))                                #taking input as list. example: [11,20,'hai12','25',['bye',40],[10]]
summ = 0                                                         #initializing sum variable as 0 because there might not be any integer or string of integers
for ele in list:                                                 #iterating through each element in the list
    if isinstance(ele,int):                                      #checking if the element is an integer 
        summ+=int(ele)                                           #adding the integer to the sum variable
    elif isinstance(ele,str) and ele.isdigit():                  #checking if the element is a string and if it contains only digits
        summ+=int(ele)                                           #adding the string of integers to the sum variable
print(summ)                                                      #printing the sum of integers and string of integers


#1st iteration: list = [11,20,'hai12','25',['bye',40],[10]], ele = 11, isinstance(ele,int) = True, summ = 0 + 11 = 11
#2nd iteration: list = [11,20,'hai12','25',['bye',40],[10]], ele = 20, isinstance(ele,int) = True, summ = 11 + 20 = 31
#3rd iteration: list = [11,20,'hai12','25',['bye',40],[10]], ele = 'hai12', isinstance(ele,int) = False, isinstance(ele,str) = True, ele.isdigit() = False, summ = 31
#4th iteration: list = [11,20,'hai12','25',['bye',40],[10]], ele = '25', isinstance(ele,int) = False, isinstance(ele,str) = True, ele.isdigit() = True, summ = 31 + 25 = 56
#5th iteration: list = [11,20,'hai12','25',['bye',40],[10]], ele = ['bye',40], isinstance(ele,int) = False, isinstance(ele,str) = False, summ = 56
#6th iteration: list = [11,20,'hai12','25',['bye',40],[10]], ele = [10], isinstance(ele,int) = False, isinstance(ele,str) = False, summ = 56
#output: 56