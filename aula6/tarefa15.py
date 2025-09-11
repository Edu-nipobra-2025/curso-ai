numeralia = []

for _ in range(5):
        numero = float(input("Digite um número: "))
        numeralia.append(numero)

for numero in numeralia:
        print(numero)

print("Média aritmética: ",(sum(numeralia)/ 5))
