def factorial(n,depth=0):
    indent=" "*depth
    print(f"{indent} CALL factorial1({n})")
    if n==0:
        print(f"{indent}RETURN 1")
        return 1
    else:
        result=n*factorial(n-1,depth+1)
    
    print(f"{indent} RETURN {result}")
    return result 
print(factorial(5))               