'''Task 4:

You are given a list of integers that contains duplicate values.
Write a Python program to:
Print the set to remove all duplicate elements

Input
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
'''



#given input
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3,0,0]
# empty list []
numbers1=[]
for i in numbers:   # loop the numbers
    if i not in numbers1:   #check the number is there or not
        numbers1.append(i)  # add number to the list
print(numbers1)    # convert list to set