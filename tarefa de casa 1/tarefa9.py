def calculadora(a,b,operacao):
    if operacao == "+":
        return a+b 
    elif operacao == "-":
        return a-b
    elif operacao == "*":
        return a*b
    elif operacao == "/":
        return a/b

operacao = input("Digite seu tipo de operação")
a = float(input("Digite seu primeiro valor"))
b = float(input("Digite seu segundo valor"))

resultado = calculadora (a,b,operacao)
print(resultado)