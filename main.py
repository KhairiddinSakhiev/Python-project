def Polindrom(n):
    reversed_n = n[::-1]
    if n==reversed_n:
        return True
    else:
        return False

def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f*=i

    return f

fact1 = Factorial(23)
pol1 = Polindrom("1231")
print(fact1)
print(pol1)