num = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = 1

while contador <= num:
    fatorial *= contador
    contador += 1

print("O fatorial de",num, " é ", fatorial)