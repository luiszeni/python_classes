senha = "oimundo"
senhaDigitada = raw_input("digite a senha")

while senhaDigitada != senha:
    senhaDigitada = raw_input("acesso negado, digite a senha novamente")
    
print "Acesso permitido"