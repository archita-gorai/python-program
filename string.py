s=input("Enter user id:")
if s.isupper():
  
 if s.startswith("USER"):
  
  if s[4:7].isnumeric():
    if not s[7].isalnum():
     print("The user id is valid")
    else:
       print("The user id is invalid")
  else:
       print("The user id is invalid")
 else:
       print("The user id is invalid")
           
         
     
