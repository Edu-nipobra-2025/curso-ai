import math

def area_quadrado(lado):
    return lado ** 2

def area_retangulo(base, altura):
    return base * altura

def area_circulo(raio):
    return math.pi * raio ** 2

print("Escolha a figura geométrica:")
print("1 - Quadrado")
print("2 - Retângulo")
print("3 - Círculo")
opcao = int(input("Digite a opção (1, 2 ou 3): "))

if opcao == 1:
    lado = float(input("Digite o lado do quadrado: "))
    print("A área do quadrado é", area_quadrado(lado), "unidades quadradas.")
elif opcao == 2:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    print("A área do retângulo é", area_retangulo(base,altura), "unidades quadradas.")
elif opcao == 3:
    raio = float(input("Digite o raio do círculo: "))
    print("A área do círculo é", area_circulo(raio), "unidades quadradas.")
else:
    print("Opção inválida! Escolha entre 1, 2 ou 3.")