#FIBONACCI SERIES USING RECURSION 

def fib( n):
    if n==0:
       return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print("using recursion",fib(4))


#Fibonacci series using iteretions

def fibiter(n):
    a=0
    b=1
    if n==0:
        return a
    for i in range(2,n+1):
        next=a+b
        a=b
        b=next
    return b
    

print("with iteration",fibiter(4))