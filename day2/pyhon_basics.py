Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="string"
  b=10
  
SyntaxError: unexpected indent
print(a)
string
print(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
print("hello")
hello
  print("hi")
  
SyntaxError: unexpected indent
#single line commens
 """multiline code"""
 
SyntaxError: unexpected indent
""" multiline comments"""
' multiline comments'
'''multiline comments'''
'multiline comments'
a="123"
b=int(a)
print(b)
123
c=10+a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c=10+a
TypeError: unsupported operand type(s) for +: 'int' and 'str'
c=10+b
prin(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    prin(c)
NameError: name 'prin' is not defined. Did you mean: 'print'?
c=10+b
print(c)
133
a=10
b=10.2
print(a+b)
20.2
print(type(a+b))
<class 'float'>
<class 'float'>
SyntaxError: invalid syntax
list=[1,2,3,4]
print(list)
[1, 2, 3, 4]
print(listt.append(5))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(listt.append(5))
NameError: name 'listt' is not defined. Did you mean: 'list'?
print(list.append(5))
None
None

l2=list.append(5)
print(l2)
None
l2=list.append[5]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l2=list.append[5]
TypeError: 'builtin_function_or_method' object is not subscriptable
l2=list.append([5])
print(l2)
None
se={1,1,1,1}
print(se)
{1}
s={1,2,3}
s.add(4)
s.remove(2)
print(s)
{1, 3, 4}
list.append(4)
print(list)
[1, 2, 3, 4, 5, 5, [5], 4]
fs=frozenset([1])
print(fs)
frozenset({1})
fs.add(5)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    fs.add(5)
AttributeError: 'frozenset' object has no attribute 'add'

======================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/list_methods.py =======================================

======================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/list_methods.py =======================================
[1, 100, 2, 3, 4, 9, 5, 6]

======================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/list_methods.py =======================================
1
[1, 100, 2, 3, 4, 9, 5, 6]

== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/tuple_methods.py ==
2
4

=== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py ===
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py", line 2, in <module>
    s.add(5)
NameError: name 's' is not defined. Did you mean: 's1'?

=== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py ===
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py", line 3, in <module>
    s1.remove(6)#error because 6 is no tere in list
KeyError: 6

=== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py ===
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py", line 4, in <module>
    s1.remove(6)#error because 6 is no tere in list
KeyError: 6

=== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py ===

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py =======================================
{1, 2, 3, 5}

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py =======================================
{1, 2, 3, 5}
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py", line 8, in <module>
    print(difference(s2))
NameError: name 'difference' is not defined

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py =======================================
{1, 2, 3, 5}
{3, 5}

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/set_methods.py =======================================
{1, 2, 3, 5}
{3, 5}
{1, 2, 3, 5}

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py", line 3, in <module>
    print(get(name))
NameError: name 'get' is not defined. Did you mean: 'set'?

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py", line 3, in <module>
    print(d.get(name))
NameError: name 'name' is not defined

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
aravind

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
None

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
None
dict_keys(['name', 'age', 'address'])
dict_values(['aravind', '26', 'hyd'])
dict_items([('name', 'aravind'), ('age', '26'), ('address', 'hyd')])

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
None
dict_keys(['name', 'age', 'address'])
dict_values(['aravind', '26', 'hyd'])
dict_items([('name', 'aravind'), ('age', '26'), ('address', 'hyd')])
26

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
None
dict_keys(['name', 'age', 'address'])
dict_values(['aravind', '26', 'hyd'])
dict_items([('name', 'aravind'), ('age', '26'), ('address', 'hyd')])
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py", line 7, in <module>
    print(d.pop("26"))
KeyError: '26'

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
None
dict_keys(['name', 'age', 'address'])
dict_values(['aravind', '26', 'hyd'])
dict_items([('name', 'aravind'), ('age', '26'), ('address', 'hyd')])
26
('address', 'hyd')

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/dict_metods.py =======================================
{'name': 'aravind', 'age': '26', 'address': 'hyd'}
None
dict_keys(['name', 'age', 'address'])
dict_values(['aravind', '26', 'hyd'])
dict_items([('name', 'aravind'), ('age', '26'), ('address', 'hyd')])
26
('address', 'hyd')
{'name': 'aravind'}

======================================= RESTART: C:\Users\upput\OneDrive\Desktop\persistance\day2\list_methods.py =======================================
1
[1, 100, 2, 3, 4, 9, 5, 6]

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/info.py ===========================================
pravalika
22
guntur
pravalika
22
guntur

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/info.py ===========================================
pravali
22
guntur
pravali
22
guntur
pravali
22


=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/info.py ===========================================
pravalika
22
guntur
pravalika
22
guntur
pravalika
22
guntur.
z=3+4j
print(typr(z))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(typr(z))
NameError: name 'typr' is not defined. Did you mean: 'type'?
print(type(z))
<class 'complex'>

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/slice.py ==========================================
revature
r
eva
REVATURE
erutaver

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/slice.py ==========================================
revature
r
eva
REVATURE
erutaver
reva
rev
reva
vature
e
ur

= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/range.py
[1, 3, 5, 7, 9]

= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/range.py
[5, 10, 15, 20, 25, 30, 35, 40, 45]

= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/range.py
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/range.py
range(5, 55, 5)

= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/range.py
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9]
c=bytes([65,66,67])
print(c)
b'ABC'
y
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    y
NameError: name 'y' is not defined
x=none
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x=none
NameError: name 'none' is not defined. Did you mean: 'None'?
p=None
print(type(p))
<class 'NoneType'>

============================================ RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/two.py ===========================================
aditya
def f1(num):
    d1=30
print(d1)
SyntaxError: invalid syntax
def f1(num):
    d1=30
    print(d1)
f1(3)
SyntaxError: invalid syntax
a=f1(3)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a=f1(3)
NameError: name 'f1' is not defined
print(a)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/operators.py ========================================
10
20
30
-10
200
10
0.5
0
100000000000000000000

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12
10
20
10.0
0.0
0.0

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12
10
20
10.0
0.0
0.0
True
False
False
True
False
True
x=10
print(x)
10
del x
print(x)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(count(keyword.kwlist))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(count(keyword.kwlist))
NameError: name 'count' is not defined. Did you mean: 'round'?
a=100
b=33

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/ifelifelse.py ========================================
a is grater

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/positive.py =========================================
positive

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5


=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5


=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5
4

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
3
1

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
3
1

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5
4
3
3
2
1
1

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
5
3
1

=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/while.py ==========================================
5
3
1

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/iteration.py ========================================
1 4
1 5
2 4
2 5

========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/iterdict.py =========================================
hyd
andhra
gujarath

========================================= RESTART: C:\Users\upput\OneDrive\Desktop\persistance\day2\operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12
10
20
10.0
0.0
0.0
True
False
False
True
False
True
2
10

========================================= RESTART: C:\Users\upput\OneDrive\Desktop\persistance\day2\operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12
10
20
10.0
0.0
0.0
True
False
False
True
False
True
2
10
Traceback (most recent call last):
  File "C:\Users\upput\OneDrive\Desktop\persistance\day2\operators.py", line 32, in <module>
    print(i in m)
NameError: name 'i' is not defined. Did you mean: 'id'?

========================================= RESTART: C:\Users\upput\OneDrive\Desktop\persistance\day2\operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12
10
20
10.0
0.0
0.0
True
False
False
True
False
True
2
10
True

========================================= RESTART: C:\Users\upput\OneDrive\Desktop\persistance\day2\operators.py ========================================
10
2
12
8
20
0
5.0
5
100
12
10
20
10.0
0.0
0.0
True
False
False
True
False
True
2
10
True
True

========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/global.py ==========================================
30
10

========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/global.py ==========================================
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/global.py", line 8, in <module>
    f1()
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/global.py", line 4, in f1
    z=x+y
UnboundLocalError: local variable 'y' referenced before assignment

========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/global.py ==========================================
30
10

========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/global2.py =========================================
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/global2.py", line 1, in <module>
    from Global import x
ModuleNotFoundError: No module named 'Global'

========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/global2.py =========================================
30
10
10

========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/global2.py =========================================
30
10
30
n=raw_input()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    n=raw_input()
NameError: name 'raw_input' is not defined
print "hlo"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("heelo world!")
heelo world!

======================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/calculator.py ========================================
30
-10
200
0.5
0
10
>>> 
====================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/temp_converter.py ======================================
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/temp_converter.py", line 6, in <module>
    celsius_tofahrenheit(100)
NameError: name 'celsius_tofahrenheit' is not defined. Did you mean: 'celsius_to_fahrenheit'?
>>> 
====================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/temp_converter.py ======================================
212.0
36.666666666666664
>>> 
====================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/age_calculater.py ======================================
23
>>> 
====================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/age_calculater.py ======================================
Enter your birth year: 2002
23
>>> 
============================================ RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/si.py ============================================
200000
>>> 
========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/areas_cal.py ========================================
Traceback (most recent call last):
  File "C:/Users/upput/OneDrive/Desktop/persistance/day2/areas_cal.py", line 9, in <module>
    area_circle=pi*r**2
NameError: name 'pi' is not defined
>>> 
========================================= RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/areas_cal.py ========================================
731.0
4212
113.09733552923255
>>> 
=========================================== RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/grade.py ==========================================
A
>>> 
============================================ RESTART: C:/Users/upput/OneDrive/Desktop/persistance/day2/tip.py ===========================================
