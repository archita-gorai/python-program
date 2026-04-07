def pat(n,depth=0,s=""):
    indent=" "*depth
    if n==0:
        return 
    else:
        for i in range(n):
            s=s+"*"
        print(f"{indent}{s}")
        return pat(n-1,depth+1,"") 
a=(int)(input("Enter limit:"))
pat(a)    
