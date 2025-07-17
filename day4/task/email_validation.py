import re

email = "example@email.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
