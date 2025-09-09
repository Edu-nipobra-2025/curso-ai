def numbsecr(num):
 return num
valorfin = 0

valorEscondido = numbsecr(7)
while  valorfin <= 7 or valorfin >= 7:
     adiv = int(input("Digite o número secreto "))
     valorfin = adiv
     if adiv < 7:
        print("Valor baixo!")
     if adiv > 7:
          print("Valor alto!")
     else:
          print("Correto!")
          break 