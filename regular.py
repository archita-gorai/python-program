import re
user=input("enter user id:")
pattern=r"^user\d{3}[^A-Za-z0-9][A-Za-z]+$"

if re.fullmatch(pattern,user):
    print("VALID")
else:
    print("INVALID")
        