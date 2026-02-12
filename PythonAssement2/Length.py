'''
Docstring for Length

2)Group Words by Length
Write a function that groups a list of words based on their length.
The function should return a dictionary where:
Keys represent word lengths.
Values are lists of words having that length.
Example:
words = ["cat", "dog", "elephant", "bat", "ant"]

# Expected:
# {
#   3: ["cat", "dog", "bat", "ant"],
#   8: ["elephant"]
# }


'''
def group(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

words = ["cat", "dog", "elephant", "ball","bat", "ant"]
print(group(words))
