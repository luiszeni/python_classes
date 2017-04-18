n = int(raw_input("informe numero "))

soma = 0;
for i in range(1, n+1):
    if n == i:
        print str(i),
    else:
        print str(i) + " +",

    soma = soma + i
    

print " = " +  str(soma)
