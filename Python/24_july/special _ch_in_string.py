#wap to check how many special characters are present in string

str = input("Enter String : ")                                       #we take input from user. example: "H@r$h !123"

count = 0                                                            #we initialize count to 0 incase there is no special characters.
for ele in str:                                                      #we iterate through each element in the string.
    if not ele.isalnum() : # if ele.isalnum()==False:                     
        count+=1                                                     #if the 1st element (H) is alphanumeric, we do not increment the count.
                                                                     #if the 2nd element (@) is not alphanumeric, we increment the count by 1.
                                                                     #if the 3rd element (r) is alphanumeric, we do not increment the count.
                                                                     #if the 4th element ($) is not alphanumeric, we increment the count by 1.
                                                                     #we continue this process until we reach the end of the string.
print(count)                                                         #finally we print the count of special characters in the string.