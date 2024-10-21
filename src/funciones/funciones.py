'''
@author: Galocha
'''

from us.lsi.tools import Preconditions
import math

def ejercicio1(n:int, k:int) -> int:
    Preconditions.check_argument(n>=k, "N tiene que ser mayor o igual que k")
    res:int = 1
    for i in range(0,k):
        res = res*(n-i+1)
    return res

def ejercicio2(a:int, r:int, k:int) -> int:
    producto = 1
    for n in range(0, k+1):
        e = a*(r**n)
        producto = producto*e
    return producto

def ejercicio3(n:int, k:int) -> float:
    Preconditions.check_argument(n>=k, "N tiene que ser mayor o igual que k")
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))     #fórmula del número combinatorio: (n sobre k) = n!/(k!(n-k)!)

def ejercicio4(n:int, k:int) -> float:
    Preconditions.check_argument(n>=k, "N tiene que ser mayor o igual que k")
    suma:int = 0
    for i in range(0, k):
        x:float = (-1)**i
        y:float = math.factorial(k+1) // (math.factorial(i+1) * math.factorial((k+1) - (i+1)))
        z:float = (k-i)**n
        suma = suma + int(x + y + z)
    return suma/math.factorial(k)


#definir f(x) y f'(x) para usarlas después

def f(x:int) -> int:
    return x**2 - 2

def fp(x:int) -> int:
    return 2*x

def ejercicio5(a:float, epsilon:float , f, fp) -> float:
    x = a
    while abs(f(x)) > epsilon:
        x = x - f(x) / fp(x)
    return x

