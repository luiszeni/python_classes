# -*- coding: utf-8 -*-
numerosLidos = []
numerosProcessados = []

N = int(raw_input("digite a quantidade de numeros"))

for i in range(0,N):
    num = int(raw_input("digite o numero " + str(i + 1) + ": "))
    numerosLidos.append(num);
    numerosProcessados.append(False)


for i in range(0,N):  
    if not numerosProcessados[i]:
        cont = 0
        for j in range(i, N):
            if numerosLidos[i] == numerosLidos[j]:
                cont = cont + 1
                numerosProcessados[j] = True 
        print str(numerosLidos[i]) + " = " + str(cont) +  ", ",   