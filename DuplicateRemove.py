'''Task 4:

You are given a list of integers that contains duplicate values.
Write a Python program to:
Convert the given list into a set
Print the set to remove all duplicate elements

Input
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

Expected Output
{1, 2, 3, 4, 5, 6}'''



#given input
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
# empty list []
numbers1=[]
for i in numbers:
    if i not in numbers1:
        numbers1.append(i)
print(set(numbers1))