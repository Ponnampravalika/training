"""class Public:
    def __init__(self):
        self.name="aditya"
    def display_name(self):
        print(self.name)
obj=Public()
obj.display_name()
print(obj.name)"""
"""class Protected:
    def __init__(self):
        self._age=30
class Subclass(Protected):
    def display_age(self):
        print(self._age)
obj=Subclass()
obj.display_age()"""
class Private:
    def __init__(self):
        self.__salary=10000
class Subclass(Private):
    def display_salary(self):
        print(self.__salary)
obj=Subclass()
obj.display_salary()
    
    
    
    

    
    
    
