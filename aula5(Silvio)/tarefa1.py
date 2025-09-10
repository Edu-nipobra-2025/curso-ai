quantidadeDeNumeros = int(input("Digite a quantidade de números: "))
vetorDeNumeros = []
for _ in range (quantidadeDeNumeros):
    vetorDeNumeros.append(float(input("número: ")))
# append manda números para um vetor ao receber um número
soma = sum (vetorDeNumeros)
media = soma / quantidadeDeNumeros if quantidadeDeNumeros > 0 else 0
print("A soma dos valores é: ", soma, "E a média é: ", media)