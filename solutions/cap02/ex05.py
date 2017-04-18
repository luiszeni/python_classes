GA = float(raw_input("digite o GA "))
GB = float(raw_input("digite o GB "))

media = (GA + 2*GB)/3

if media >= 6.0:
    print "APROVADO"
else:
    print "Recuperacao"
    GC = float(raw_input("digite o GC "))
    
    media1 = (GC + 2*GB)/3
    media2 = (GA + 2*GC)/3
    
    if media1 > media2:
        if media1 >= 6.0:
            print "APROVADO"
        else:
            print "REPROVADO"
    else:
        if media2 >= 6.0:
            print "APROVADO"
        else:
            print "REPROVADO"