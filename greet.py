class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("HEllo from B")
class C(A):
    def greet(self):
        print("HEllo from C")                
class D(B,C):
    pass
a=D()
a.greet() 
A.greet(a)
super(B,a).greet()
