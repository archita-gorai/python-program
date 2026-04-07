class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def store(self):
        l1=list()
        l1.append(self.name)
        l1.append(self.roll)
        l1.append(self.marks)
        return l1
s1=student("A",1,70)
s2=student("B",2,49)
s3=student("C",3,87)
s4=student("D",4,57)
s5=student("E",5,89)
l1=[s1.store(),s2.store(),s3.store(),s4.store(),s5.store()]
print("Students who got more than 80:")
for i in range(len(l1)):
    if l1[i][2]>80:
        print(l1[i])

       