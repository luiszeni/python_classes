a = int(raw_input("digite o n1 "))
b = int(raw_input("digite o n2 "))
c = int(raw_input("digite o n3 "))


if a < b and b < c:
    print str(a) + " " + str(b) + " " + str(c)
elif a < c and c < b:
    print str(a) + " " + str(c) + " " + str(b)
elif b < a and a < c:
    print str(b) + " " + str(a) + " " + str(c)
elif b < c and c < a:
    print str(b) + " " + str(c) + " " + str(a)
elif c < a and a < b:
    print str(c) + " " + str(a) + " " + str(c)
elif c < b and b < a:
    print str(c) + " " + str(b) + " " + str(a)
else:
    print "tem caras iguais"