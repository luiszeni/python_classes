x = float(raw_input("digite o x "))
y = float(raw_input("digite o y "))
z = float(raw_input("digite o z "))

if x > y + z or y > x + z or z > y + x:
    print "triangulo invalido"
else:
    print  "tringulo valido"
    
    if x == y and y == z:
        print "equilatero"
    elif x !=y and y != z and z != x:
        print "escaleno"
    else:
        print "isoscele"