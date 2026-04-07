def total(a):
    p=0
    if a<=100:
        p=a*1
        print("Units charged(Rs.1/unit):",a)
        print("Total bill:",p)
    elif a>100 and a<=200:
        p=100*1
        print("Units charged(Rs.1/unit):",100)
        print("Price:",p)
        a=a-100
        p=(a)*2
        print("Units charged(Rs.2/unit):",a)
        print("Price:",p)
        p=100*1+a*2
        print("Total bill:",p)
    elif a>200:
         p=100*1
         print("Units charged(Rs.1/unit):",100)
         print("Price:",p)
         a=a-100
         p=100*2
         print("Units charged(Rs.2/unit):",100)
         print("Price:",p)
         a=a-100
         p=a*5
         print("Units charged(Rs.5/unit):",a)
         print("Price:",p)
         p=100*1+100*2+a*5
         print("Total bill:",p)   
units=(int)(input("Number of units:"))
total(units)
