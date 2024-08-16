class Cat:
    def __init__(self, color):
        self.color = color
    
    @classmethod
    def generate(cls, dad, mom):
        return cls(dad.color + ' and ' + mom.color)

dad = Cat(color='black')
mom = Cat(color='white')
child = Cat.generate(dad, mom)
print(child.color)