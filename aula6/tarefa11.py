numero = []

for _ in range(5):
        numeroAux = float(input("Digite um número: "))
        numero.append(numeroAux)


print(numero)
for _ in range(4,-1,-1):
        print(numero[_])
