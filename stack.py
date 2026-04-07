class stack:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
b1=stack()
a=int(input("Enter an element"))
b1.push(a)
while(a!=0):
     a=int(input("enter an element"))
     b1.push(a)
b1.pop()
print(b1.items)     
print(f"Last element to be inputed:{b1.pop()}") 
print(b1.isEmpty())
print(b1.size())          