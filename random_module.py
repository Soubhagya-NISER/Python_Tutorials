import random

for i in range(3):
    print(random.random())  # Random float between 0.0 to 1.0
    print(random.randint(10,20))

members  = ['John','Harry','Bob','SD']
leader = random.choice(members)
print(leader)  # Randomly select a member from the list

 
class Dice:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def roll(self):
        a = (self.x,self.y)
        return a

m = random.randint(1,6)
n = random.randint(1,6)   
dice = Dice(m,n)

print(dice.roll())
