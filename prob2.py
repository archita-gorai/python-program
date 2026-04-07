#create a class vector x and y overload add to add operators, output should be in x,y
class Vector:
    def __init__(self,values):
        self.values=values

    def __add__(self,other):
        return ((self.values[0]+other.values[0],self.values[1]+other.values[1]))
    def __str__(self):
        return (self.values)

s=Vector(2,3)
s2=Vector(5,6)
r=(s.x+s2.x,s.y+s2.y)
print(f"Vector sum is {r}")