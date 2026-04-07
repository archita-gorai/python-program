class A:
    def greet(self):
        print("Hello from A")
class B:
    def greet(self):
        print("HEllo from B")
class C:
    def greet(self):
        print("HEllo from C")                
class D(B,C):
    pass
a=D()
a.greet()    