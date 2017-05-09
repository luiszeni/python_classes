# -*- coding: utf-8 -*-
from math import pi

def calculaAreaCirculo(raio):
    area = raio**2 * pi
    return area
    
def calculaAreaRetangulo(altura, largura):
    area = altura * largura
    return area
    
def calculaAreaTriangulo(base, altura):
    area = (base*altura)/2
    return area

def menu():
    print "Calculadora de Areas, escolha a opcao:"
    print "Circulo"
    print "Triangulo"
    print "Retangulo"
    print "Sair"
    return raw_input("Qual opcao voce deseja?: ")



op = "bla"
while  op != "Sair":
    op = menu()
    area = 0;
    if op == "Triangulo":
        b = float(raw_input("informe a base: "))
        a = float(raw_input("informe a altura: "))        
        area = calculaAreaTriangulo(b,a)
    elif op == "Circulo":
        r = float(raw_input("informe o raio: "))
        area = calculaAreaCirculo(r)
    elif op == "Retangulo":
        a = float(raw_input("informe a altura"))
        l = float(raw_input("informe a largura"))
        area = calculaAreaRetangulo(a, l)
    elif op == "Sair":
        print "Saindo do Progama"
        continue
    else:
        print "Opção inválida... "
        continue
            

    print "area do " + op +  " calculada = " + str(area)

