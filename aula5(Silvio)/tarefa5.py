candidatos = ["maria", "joao"]
votagem = []

while True:
    votagemResultado = input("Vote por algum candidato (maria ou joao). Caso queira acabar a votação, escreva 'fim': ")
    
    if votagemResultado == "fim":
        print("Acabou a votação!")
        break
    elif votagemResultado in candidatos:
        votagem.append(votagemResultado)
    else:
        print("Candidato inválido, apenas escreva 'maria' ou 'joao'.")

print("\nTodos os votos:", ", ".join(votagem))
votosMaria = votagem.count("maria")
votosJoao = votagem.count("joao")
print("Votos Maria:", votosMaria)
print("Votos João:", votosJoao)
print("Votos Totais:", len(votagem))

if votosMaria > votosJoao:
    print("Maria venceu a eleição!")
elif votosJoao > votosMaria:
    print("João venceu a eleição!")
else:
    print("Empate!")
