from numpy import *
def esPrimo(n):
    if n < 2:
        return False
    else:
        arr = arange(2,int(n**(1/2)+1))
        c = 0
        for i in arr:
            if n%i == 0:
                c = c + 1
        if c == 0:
            return True
        else:
            return False
def esPrimoGaussiano(a,b):
    if (a == 0):
        if (abs(b)%4 == 3):
            return True
    if (b == 0):
        if (abs(a)%4 == 3):
            return True
    if (a!=0 and b!=0):
        n = (a**2) + (b**2)
        if esPrimo(n):
            return True
    return False
r = 5
arr = arange(-r,r+1)
for a in arr:
    for b in arr:
        p = a**2 + b**2
        if (p <= r**2):
            if esPrimoGaussiano(a,b):
                x = complex(a,b)
                print(x)
