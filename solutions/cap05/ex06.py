# -*- coding: utf-8 -*-

def fatorial(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod
    
def fatRec(n):
    if n > 1:
        return n * fatRec(n-1)
    return 1;


N = int(raw_input("digite N"))
print  str(fatRec(N)) + "!"
