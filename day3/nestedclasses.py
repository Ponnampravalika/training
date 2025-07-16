class Color:
    def __init__(self):
        self.name="green"
        self.lg=self.LightGreen()
        
    def show(self):
        print("name:",self.name)
    class LightGreen:
        def __init__(self):
            self.name="light green"
            self.code="024avc"
        def display(self):
            print('name:',self.name)
            print('code:',self.code)
outer=Color()
outer.show()
g=outer.lg
g.display()
            
