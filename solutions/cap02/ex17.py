d = int(raw_input("digite o dia "))
m = int(raw_input("digite o mes "))
a = int(raw_input("digite o ano "))

tDias = 30
valido = True

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    tDias = 31
elif m == 2:
    if a%4 == 0:
        tDias = 29
    else:
        tDias = 28
elif m < 1 or m > 12:
    print "mes invalido"
    valido = False
    
if d < 1 or d > tDias:
    print "dia invalido"
    valido = False

if valido:
    print "data valida"

