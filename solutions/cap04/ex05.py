# -*- coding: utf-8 -*-

lista1 = []
lista2 = []
lista3 = []

for i in range(0,10):
    lista1.append(int(raw_input("Digite o valor " + str(i) +  " da lista 1" )))
    lista2.append(int(raw_input("Digite o valor " + str(i) +  " da lista 2" )))
    
for i in range(0,10):
    lista3.append(lista1[i] * lista2[i])
    
print lista1
print lista2
print lista3