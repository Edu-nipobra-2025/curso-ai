
n = int(input("Quantos elementos o etor deve ter?"))
vetor = []

for i in range(n):
    valor = float(input("Digite o próximo valor"))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)
soma = sum (vetor)
media = soma/n
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")
print(f"Média: {media}")
