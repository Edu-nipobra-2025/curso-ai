numeralia = []

while True:
 numeros = int(input("Digite vários numeros maiores ou menores que 0, escreva 0 caso queira parar a soma."))
 if numeros == 0:
        print("Pegue sua conta!")
        break
 else:
        numeralia.append(numeros)


print("A soma total é",sum(numeralia))
