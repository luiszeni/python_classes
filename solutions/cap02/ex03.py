v = float(raw_input("digite o total de vendas "))

if v > 50000:
    print "a comicao eh: " + str(v * 0.12)
elif v >= 30000 and v <= 50000:
    print "a comicao eh: " + str(v * 0.95)
elif v >= 0:
    print "a comicao eh: " + str(v * 0.7)
else:
    print "valores negativos são invalidos"
    
