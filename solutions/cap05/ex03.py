def calculaAreaTriangulo(base, altura):
    area = (base*altura)/2
    return area
    
b = float(raw_input("informe a base: "))
a = float(raw_input("informe a altura: "))

area = calculaAreaTriangulo(b,a)
print "area do triagulo " + str(area)
