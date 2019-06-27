def Fibonacci(n):
    if(n>=2):
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    elif (n==0 or n==1):
        return 1
    else:
        return -1

# print Fibonacci(20)

print Fibonacci(647)