import re
pattern=re.compile(r"")
a=input("Enter a sentence:")
pattern=re.compile(r"\D")
result=pattern.sub(" ",a)
print(result)
p2=re.compile(r"\d+")
l1=list()
l1=p2.findall(result)
s=0
for i in l1:
    s+=int(i)
print(f"Numbers found:{l1}")
print(f"Total sum is:{s}")
