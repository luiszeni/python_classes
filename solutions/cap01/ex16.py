from math import sqrt

x1 = float(raw_input("digite x1: "))
y1 = float(raw_input("digite y1: "))

x2 = float(raw_input("digite x2: "))
y2 = float(raw_input("digite y2: "))

interno = (x1 - x2) ** 2 + (y1 - y2) ** 2
d = sqrt(interno)

print "a distancia entre os pontos eh: " + str(d)
