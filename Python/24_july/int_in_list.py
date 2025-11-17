#WAP to print how many integers are present in list.

list = eval(input('Enter list : '))                                 #we take input list from user. example [1,2,3,'a','b','c',4,5,6]

count = 0                                                           #we initialize count to 0 because there might be no integers in the list.
for ele in list:                                                    #in the for loop we iterate through each element in the list.
    if type(ele)==int: # if isinstance(ele,int): 
        count+=1                                                    #we check if the element is of type integer or not.
                                                                    #if it is then we increase the count by 1 and move to next element.
                                                                    #if it is not then we move to next element without increasing the count.

print(count)                                                        #we print the count of integers in the list.