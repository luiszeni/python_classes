# -*- coding: utf-8 -*-

def mostraTabuada(n):
    for i in range(1, n+1):
        print str(i) + " x " + str(n) + " = " + str(i*n) 
    

N = int(raw_input("digite N"))
mostraTabuada(N)
