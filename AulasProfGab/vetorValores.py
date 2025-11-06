n = int(input("Digite a quantidade de números: "))
vetorDeNumeros = []
for i in range (n):
    v = int(input("digite qualquer valor "))
    vetorDeNumeros.append(v)

print("\n--- Números Pares Digitados ---")

for v in vetorDeNumeros:
    if v % 2 == 0:
        print(v)
