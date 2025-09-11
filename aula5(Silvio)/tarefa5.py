maria = 0
joao = 0
candidato = [maria, joao]

votoJoao = maria
votoMaria = joao
votoTotal = 0
while True:
 votagem = input("vote por algum canditado (maria ou joao), caso queira acabar a votação, escreva fim ")
 if votagem == "joao":
  votoJoao += 1
  votoTotal += 1
  continue 
 elif votagem == "maria":
  votoMaria += 1
  votoTotal += 1
 if votagem == "fim":
  "Acabou a votação!"
  break

print("Votos joão: ",votoJoao,"\nVotos Maria: ",votoMaria,"\nVotos Totais: ",votoTotal)
  