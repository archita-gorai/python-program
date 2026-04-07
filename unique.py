s=input("Enter a sentence:")
s+=" "
l=s.split(" ")
l1=list()
i=0
t=len(l)
for i in range(t):

 if l[i] not in l[1:t+1]:
    l1.append(l[i])
    print(l1)
    i+=1
    
