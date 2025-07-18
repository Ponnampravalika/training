x=10
def f1():
   global z
   y=20
   z=x+y
   print(z)

f1()
print(x)
