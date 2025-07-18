import re

url = "https://www.google.com"
pattern = r'^https?://[^\s/$.?#].[^\s]*$'

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")
