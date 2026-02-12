'''Task 3:

Write a Python program to print all prime numbers up to a given number N.
Requirements
Take an integer input N

Print all prime numbers from 2 to N (inclusive)'''


# take input from keyboard
N=int(input("Enter a number :"))
# take the range 1 to upto number
for num in range(1,N+1):
    count=0  #count number factors
    for i in range(1,num+1):
        if num%i==0:   #check the prime or not it completely divided,it prime
            count +=1
    if count==2:       #prime number exactly 2 factors (itself and 1)
        print(num)


'''N = int(input("Enter a number: "))

for num in range(2, N + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:          # runs only if loop didn't break
        print(num)'''
