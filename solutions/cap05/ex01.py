
def calculaAreaRetangulo(altura, largura):
    area = altura * largura
    return area
    


a = float(raw_input("informe a altura"))
l = float(raw_input("informe a largura"))

area = calculaAreaRetangulo(a, l)

print "area do retangulo" + str(area)
