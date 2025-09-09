def numbsecr(num):
    return num

valorEscondido = numbsecr(7)
adiv = 0

while adiv < 5:
    tenta = int(input("Digite o número secreto: "))
    adiv += 1

    if tenta < valorEscondido:
        print("Valor baixo!")
    elif tenta > valorEscondido:
        print("Valor alto!")
    else:
        print("Correto!")
        break 
else:
    print("Tentativas esgotadas!")