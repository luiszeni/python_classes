#leitura de anos/meses/dias
a = int(raw_input("quantos anos vc viveu"))
m = int(raw_input("quantos meses vc viveu"))
d = int(raw_input("quantos dias vc viveu"))

#converter tudo para dia
total = a*365 + m*30 + d

#mostrar o total de dias
print "o total de dias vividos eh: " + str(total)

