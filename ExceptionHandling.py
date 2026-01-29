'''Task 2:

Given a list of numbers (as strings):
nums = ["10", "20", "abc", "30", "5"]
Tasks
Convert valid numbers to integers (ignore invalid values using exception handling).
1.keep only numbers greater than 10.
2.square the remaining numbers.
3.find the sum of squared values.'''

# get input
'''nums = ["10", "20", "abc", "30", "5"]
number=[]
for i in nums:    #convert string to int
    try:
        number.append(int(i))         # finding the integer
        print(i)
    except:
        print("it is not integer :",i)
square=0
for num in number:    #number greater than 10 and add squares
    if num>10:
        print(num)
        square =square+(num*num)

print(square)  
'''

from functools import reduce

nums = ["10", "20", "abc", "30", "5"]

# Step 1: convert string to int safely
number = []
for i in nums:
    try:
        number.append(int(i))
        print(i)
    except:
        print("it is not integer:", i)

#  numbers > 10
greater_than_10 = list(filter(lambda x: x > 10, number))

# print numbers > 10
list(map(lambda x: print(x), greater_than_10))

# add squares
square = reduce(lambda total, x: total + x*x, greater_than_10, 0)

print(square)



      