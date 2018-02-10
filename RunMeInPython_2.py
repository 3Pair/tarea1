from numpy import *
def esPrimo(n):
    if n < 2:
        return False
    else:
        arr = arange(2,int(n**(1/2)+1))
        for i in arr:
            if n%i == 0:
                return False
        return True
def esPrimoGaussiano(a,b):
    n2 = a**2 + b**2
    if (a*b == 0):
        n = int(n2**(1/2))
        if (n%4 == 3):
            return True
    else:
        if esPrimo(n2):
            return True
    return False
r = 5
arr = arange(-r,r+1)
for a in arr:
    for b in arr:
        if esPrimoGaussiano(a,b):
            x = complex(a,b)
            print(x)
