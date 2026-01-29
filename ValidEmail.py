'''Task 5
Write a Python program to validate email addresses using regex.
Valid format: username@domain.extension
Username: alphanumeric and underscores
Domain: alphanumeric
Extension: 2-4 letters
Test cases:
python
emails = ["user@example.com", "invalid.email", "test_123@domain.co.uk", "@nodomain.com"]'''

import re
#given input
emails = ["user@example.com", "invalid.email", "test_123@domain.co.uk", "@nodomain.com"]
for email in emails:
    if re.fullmatch(r"^[a-zA-z0-9+-]+@[a-zA-z0-9]+\.[a-zA-z]{2,4}$",email):
        print("valid email are :",email)
    else:
        print("invalid email are :",email)
