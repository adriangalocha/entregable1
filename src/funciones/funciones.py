'''
Created on 18 oct 2024

@author: Galocha
'''

from us.lsi.tools import Preconditions


def producto(n:int, k:int) -> int:
    Preconditions.check_argument(n>=k, "N tiene que ser mayor o igual que k")
    res:int = 1
    for i in range(0,k):
        res = res*(n-i+1)
    return res

def producto_secuencia_geometrica(a:int, r:int, k:int) -> int:
    producto = 1
    for n in range(0, k):
        e = a*(r**n)
        producto = producto*e
    return producto

def numero_combinatorio(n:int, k:int) -> int:
    Preconditions.check_argument(n>=k, "N tiene que ser mayor o igual que k")
    