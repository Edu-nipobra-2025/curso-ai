def nota(notaResultado):
    return notaResultado

resultado = nota

notaResultado = int(input("Digite a sua nota:\n"))

if notaResultado < 5:
    print("Reprovado")
elif notaResultado >= 5 or notaResultado <= 6.9:
 print("Recuperação")
else:
 print("Aprovado")