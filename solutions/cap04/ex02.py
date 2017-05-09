# -*- coding: utf-8 -*-
numerosLidos = []

for i in range(0,15):
    num = int(raw_input("digite o numero " + str(i + 1) + ": "))
    numerosLidos.append(num);
    
numerosLidos.sort();
    
for i in range(0,15):
    print "A posicao " + str(i) + " tem o valor " + str(numerosLidos[i])  