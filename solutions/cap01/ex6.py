#lendo os votos
b = int(raw_input("qtos votos brancos? "))
n = int(raw_input("qtos votos nulos? "))
v = int(raw_input("qtos votos validos? "))

#converte para porcentagem
#   total   -  100%
#  brancos  -  x
#  x * total =  brancos * 100
#  x = (brancos * 100)/total

t = b + n + v

pB = float(b * 100) / t
pN = float(n * 100) / t
pV = float(v * 100) / t

#mostra as porcentagens
print "porcentagem de validos = " + str(pV)
print "porcentagem de nulos = " + str(pN)
print "porcentagem de brancos = " + str(pB)