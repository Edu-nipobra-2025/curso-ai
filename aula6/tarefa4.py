def monitorIdade(idade):
    idade
    if idade < 18:
        print("Menor de idade")
    elif idade >19 and idade < 59:
        print("Adulto")
    else:
        print("idoso")
    return idade

idade = int(input("Digite sua idade: "))
monitorIdade(idade)