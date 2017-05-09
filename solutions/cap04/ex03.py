# -*- coding: utf-8 -*-
numerosLidos = []

N = int(raw_input("digite a quantidade de numeros"))

for i in range(0,N):
    num = int(raw_input("digite o numero " + str(i + 1) + ": "))
    numerosLidos.append(num);
    
for i in range(N-1, -1, -1):
    print numerosLidos[i],