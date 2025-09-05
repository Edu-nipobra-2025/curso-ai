def numbsecr(num):
 return num

adiv = int(input("Digite o número secreto "))
valorEscondido = numbsecr(7)
if  adiv == valorEscondido:
    print("Acertou!")
elif adiv > valorEscondido:
    print("muito alto!")
else:
    print("Muito baixo!")