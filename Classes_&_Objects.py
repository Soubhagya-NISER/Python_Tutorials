class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
point2 = Point()
point2.move()
point2.x = 1

print(point1.y)
print(point2.x)

class Person:
    name = 'SD'
    occupation  = 'Student'
    def info(self):
        print(f'{self.name} is a {self.occupation}')


a = Person()
b = Person()
c = Person()
a.name = 'Soubhagya Dutta'
b.name = 'Swati Ghosh'

b.occupation  = 'Teacher'

a.info()
b.info()
c.info()