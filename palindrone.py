s=input("Enter a sentence")
s1=""
l=""
i=0
j=1
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
     s1=s[i:j+1]
     r=s[::-1]
     if s1==r and len(r)>len(l):
        l=r
print(l)     
  
      
  