#WAP to print absolute difference of all even integers and odd integers present in given list.

list = eval(input('Enter list:'))                                 #we take input as list. example: [1,2,3,4,5,6,7,8,9,10]
evensum = 0                                                       #initialize sum of even numbers as 0 because list may not contain any even numbers
oddsum = 0                                                        #initialize sum of odd numbers as 0 because list may not contain any odd numbers
for ele in list:                                                  #iterate through each element in the list
    if ele % 2==0:                                                #check if the 1st element is even, if not then move to else statement and add it to oddsum
        evensum += ele                                            #check if the 2nd element is even, add it to evensum if it is even
    else:                                                         #check if the 3rd element is even, if not then move to else statement and add it to oddsum
        oddsum +=ele                                              #check if the 4th element is even, add it to evensum if it is even
                                                                  #repeat the same for all elements in the list
print('Sum of even Numbers is:',evensum)                          #print the sum of all even numbers
print('Sum of odd Numbers is:',oddsum)                            #print the sum of all odd numbers

print('Absolute Difference = ',abs(evensum - oddsum) )            #print the absolute difference of even sum and odd sum

#1st iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 1, ele % 2 == 0 = False, oddsum = 0 + 1 = 1
#2nd iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 2, ele % 2 == 0 = True, evensum = 0 + 2 = 2
#3rd iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 3, ele % 2 == 0 = False, oddsum = 1 + 3 = 4
#4th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 4, ele % 2 == 0 = True, evensum = 2 + 4 = 6
#5th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 5, ele % 2 == 0 = False, oddsum = 4 + 5 = 9
#6th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 6, ele % 2 == 0 = True, evensum = 6 + 6 = 12
#7th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 7, ele % 2 == 0 = False, oddsum = 9 + 7 = 16
#8th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 8, ele % 2 == 0 = True, evensum = 12 + 8 = 20
#9th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 9, ele % 2 == 0 = False, oddsum = 16 + 9 = 25
#10th iteration: list = [1,2,3,4,5,6,7,8,9,10], ele = 10, ele % 2 == 0 = True, evensum = 20 + 10 = 30
#Final output: Sum of even Numbers is: 30, Sum of odd Numbers is: 25, Absolute Difference = 5
#Note: abs() function is used to get the absolute value of the difference.