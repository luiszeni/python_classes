from math import pi

def calculaAreaCirculo(raio):
    area = raio**2 * pi
    return area
    

r = float(raw_input("informe o raio: "))
area = calculaAreaCirculo(r)
print "area do circulo " + str(area)
