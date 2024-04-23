def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f*=i

    return f

fact1 = Factorial(23)
print(fact1)