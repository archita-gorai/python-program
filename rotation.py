s1=input("input 1st string")
s2=input("input 2nd string")
i=0
l=""
f=1
for i in range(len(s2)):
  l=s2[1:len(s2)+1]+s2[0]
  if l==s1:
    f=0
  else:
    s2=l 
if f==0:
  print("Rotation")
else:
  print("Not rotation") 
       
