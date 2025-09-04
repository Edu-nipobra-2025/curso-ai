teste = int(input("Digite sua conversão \n 1- Farenheit pra celsius \n 2- Celsius para farenheit \n"))

if teste == 1:
 temp1 = int(input("Dê sua temperatura em Fahrenheit"))
 tempfahre = (temp1 - 32) * (5/9)
 print("Sua temperatura é:", tempfahre)
elif teste == 2:
 temp2 = int(input("Dê sua temperatura em Celsius"))
 tempcel = (temp2 * 1.8) + 32
 print("Sua temperature é:", tempcel)
else:
 print("Número inválido.")