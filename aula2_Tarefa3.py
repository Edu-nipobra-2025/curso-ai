peso = int(input("Digite seu peso para fazer o seu calculo de IMC \n"))
altura= float(input("Digite sua altura fazer o seu calculo de IMC \n"))


calculo = (peso / (altura * altura))

print ("seu IMC é:", calculo)
if calculo <= 18.5:
    print ("Magreza")
elif calculo >= 18.6 and calculo <= 24.9:
    print ("Normal")
elif calculo >= 25 and calculo <= 29.9:
    print ("Sobrepeso")
elif calculo >= 30:
    print ("Obeso")
