#input a 2d list, overload + and - for matrix add and subtract
class Matrix:
    def __init__(self,a=list()):
        self.a=a
    def __add__(self,other):
         for i in range(len(self.a)):
          return self.a[i]+other.a[i]        
    def __sub__(self,other):
         for i in range(len(self.a)):
          return self.a[i]-other.a[i]           
    def __str__(self):
        return self.a() 
l=[[1,2],[3,4]]
d=[[5,6],[8,9]]          
a=Matrix(l)  
b=Matrix(d)
l3=list()
for i in range(len(a.a)):
        for j in range(len(a.a[i])):
           l3[i][j]=a.a[i][j]+b.a[i][j]
print(l3)           