''''
Alternate Values from Multiple Lists (Round Robin)
Write a function that takes two lists and returns a new list by alternating elements from each list.
If one list is longer than the other, append the remaining elements at the end.
Example:
a = [1, 2]
b = ['a', 'b', 'c']

# Expected:
# [1, 'a', 2, 'b', 'c']
# '''

def round_robin(a, b):
    result = []
    
    i = 0
    while i < len(a) and i < len(b):
        result.append(a[i])
        result.append(b[i])
        i = i + 1
    result = result + a[i:]
    result = result + b[i:]

    return result
a=[1,2]
b=[1,'a',2,'b','c']

print(round_robin(a, b))




