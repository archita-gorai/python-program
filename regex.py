import re
pattern=re.compile(r"") 
word=input("Please enter your string:")
pattern=re.compile(r"\D+")
p2=re.compile(r"\s")
result=pattern.sub(" ",word)

print(help(pattern.match))
print(dir(pattern))
