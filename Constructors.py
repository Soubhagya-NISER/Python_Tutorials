class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')

point = Point(10,20)
print(point.x)

class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f'{self.name} is a {self.occupation}')
    def talk(self):
        print(f'Hello, I am a {self.name} and I am a {self.occupation}')

a = Person('Soubhagya Dutta', 'Student')
b = Person('Swati Ghosh', 'Teacher')
a.info()
b.info()
a.talk()
b.talk()


        
