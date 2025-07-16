"""print(len("hello"))
print(len([1,2,3]))
print(max(1,3,2))
print(max("a","2","n"))
def add(a,b):
    return a+b
print(add(3,4))
print(add("hello","world"))
print(add([1,2],[3,4]))"""
class Shape:
    def area(self):
        return "undefined"
class Rectangle(Shape):
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def area(self):
        return self.len*self.wid
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
shapes=[Rectangle(2,3),Circle(5)]
for shape in shapes:
    print(f"area:{shape.area()}")

    



