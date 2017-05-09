# -*- coding: utf-8 -*-

lista1 = []

for i in range(0,20):
    lista1.append(int(raw_input("Digite o valor " + str(i) +  " da lista: " )))
      

for i in range(19, -1, -1):
    if lista1[i] % 2 == 0:
        lista1.pop(i)
        
print lista1