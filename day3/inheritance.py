class A:
    def __init__(self,name):
        self.name=name
    def s(self):
        return "hello"
class D(A):
    def sound(self):
        return "woof"
a=A("generic animal")
d=D("buddy")
print(a.name)
print(d.name)
print(d.sound())
#print(a.sound())
print(a.s())
print(d.sound())
print(d.s())
      
