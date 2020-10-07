def Factorial(n):
    fact=1
    while n>0:
        if n ==1:
            return 1
        else:
            return n * Factorial(n-1)
print(Factorial(4))
    