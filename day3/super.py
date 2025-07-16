class Parent:
    def show(self):
        print("inside parent")
class Child(Parent):
    def show(self):
        #super().show()
        print("inside child")
obj=Child()
obj.show()
    
