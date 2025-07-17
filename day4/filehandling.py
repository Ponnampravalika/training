"""with open('file.txt','r') as f:
    content=f.read()
with open('file.txt','r') as f:
    for line in f:
        print(line.strip())
with open('file.txt','r') as f:
    lines=f.readlines()
with open('file.txt','r') as f:
    first_line=f.readline()"""
import os 
import time
with open('output.txt','w') as f:
    f.write("hello world")
with open('output.txt','r') as f:
    first_line=f.readline()
    print(first_line)

if os.path.exists('file.txt'):
    print("file exist")
size = os.path.getsize(r'C:\Users\upput\OneDrive\Desktop\persistance\day4\filehandling.py')
mod_time=os.path.getmtime('file.txt')
readable_time=time.ctime(mod_time)
print(readable_time)
 



