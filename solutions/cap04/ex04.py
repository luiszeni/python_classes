# -*- coding: utf-8 -*-
numerosLidos = []

N = int(raw_input("digite a quantidade de numeros"))

for i in range(0,N):
    num = int(raw_input("digite o numero " + str(i + 1) + ": "))
    numerosLidos.append(num);
    
    
menor = numerosLidos[0]
maior = numerosLidos[0]
soma = numerosLidos[0]
    
for i in range(1,N):
    soma = soma + numerosLidos[i]
    
    if numerosLidos[i] < menor:
        menor = numerosLidos[i]
        
    if numerosLidos[i] > maior:
        maior = numerosLidos[i]
        
print "a media é " + str(soma/N)
print "o menor numero é " + str(menor)
print "o maior numero é " + str(maior)