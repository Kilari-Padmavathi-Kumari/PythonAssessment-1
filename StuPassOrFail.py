'''Task1:
You are given a list of student records as tuples:
students = [
    ("Anil", 78),
    ("Ravi", 45),
    ("Meena", 88),
    ("Sita", 62),
    ("Raj", 49)
]

Tasks
Create a dictionary where:

key → student name

value → "Pass" if marks ≥ 50 else "Fail"

Count how many students passed and failed.'''


#give input
students = [
    ("Anil", 78),
    ("Ravi", 45),
    ("Meena", 88),
    ("Sita", 62),
    ("Raj", 49)
]
result={}   # dict to store values
pass_count=0
fail_count=0
for name,marks in students:  # get each student record like(enumerate(index,values))
    if marks >=50:           # check marks are greater than 50 or not
        result[name]='pass'  # name as key and pass is value
        pass_count +=1        # increment
    else:
        result[name]='fail'
        fail_count +=1
print(result)                   # print result in dict
print("passed : ",pass_count)
print("failed : ",fail_count)

 
