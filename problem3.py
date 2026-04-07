def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=(int)(input("Enter 1st number:"))
b= (int)(input("Enter 1st number:"))  
if(a>b): 
 print(f"The gcd of {a} & {b} is:{gcd(a,b)}")
elif(a<b):
    print(f"The gcd of {a} & {b} is:{gcd(b,a)}")