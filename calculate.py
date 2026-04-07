max_item=lambda x,y:x if x>y else y

a=int(input("Enter first no.:"))
print(max_item(a,3))

def operate(x):
    return lambda y:x+y
f=operate(10)
print(f(5))
l1=[40,50,60,70]
result=list(map(lambda x:x*2,l1))
l=list(filter(lambda x:x%2==0,l1))
print(l)
print(result)


