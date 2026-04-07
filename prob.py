#create a class student with two attribute name and marks overload greater than operator to compare

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self,other):
        return self.marks>other.marks
s=Student("A",90)
s2=Student("B",95)
if(s>s2):
  print(f"Name is {s.name} and marks{s.marks}")
        
else:
  print(f"Name is {s2.name} and marks{s2.marks}" )     

