import re
"""t="hello, my phone number is 123-456-7890"
p=r"\d{3}-\d{3}-\d{4}"
match=re.search(p,t)
if match:
    print(f"found:{match.group()}")
    print(f"position:{match.start()}-{match.end()}")"""
"""text="hello world"
p=r"hello"
match=re.match(p,text)
if match:
    print("match is found at the beganing")
else:
    print("no match is found at beganing")"""
"""text="123"
pattern=r"\d+"
if re.fullmatch(pattern,text):
    print("entire string match is pattern")"""
"""text="contact me at john@email.com or joha@emain.org"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails=re.findall(pattern,text)
print(emails)"""
"""txt="the date is 2023-12-25"
pattern=r"(\d{4})-(\d{2})-(\d{2})"
replacement=r"\2/\3/\1"
new_txt=re.sub(pattern,replacement,txt)
print(new_txt)"""
"""txt="apple,banana;orange:grape"
pattern=r"[,;:]"
parts=re.split(pattern,txt)
print(parts)"""
"""p=r"\d+"
t="i have 25 apples"
print(re.findall(p,t))"""
"""p=r"\w+"
t="hello_world 123"
print(re.findall(p,t))"""
p=r"\s+"
t="hello  world"