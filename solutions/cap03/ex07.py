# 0 1 1 2 3 5 8 13 ....

ant = 0
atu = 1
print ant, atu,

for i in range(0,48):
    prox = ant + atu
    print prox,
    
    ant = atu
    atu = prox