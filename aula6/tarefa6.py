
numero = int(input("Digite um número inteiro: "))

print("Números ímpares de 1 até", numero, ":")
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i)
