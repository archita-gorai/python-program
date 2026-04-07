class calculator:
    def multiply(self,a=1,b=1,*args):
        result=a*b;
        for num in args:
            result*=num
        return result
calc=calculator()
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=(22/7)*self.radius*self.radius
        print(f"Area=pi x r x r={a}")
class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        a=self.side*self.side
        print(f"Area=side x side={a}")
def show_area(shape):
    shape.area()
class Number:
    def __init__(self,value):
        self.value=value
    #overloading+operator
    def __add__(self,other):
        return Number(self.value+other.value)
    def __str__(self):
        return(self.value)
n1=Number(10)
n2=Number(20)
result=n1+n2
