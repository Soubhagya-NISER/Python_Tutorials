class Mammals:
    def walk(self):
        print("walk")
class Dog(Mammals):
    def bark(self):
        print("bark")
    
class Cat(Mammals):
    def be_annoying(self):
        print("annoying")

dog = Dog()
cat = Cat()
