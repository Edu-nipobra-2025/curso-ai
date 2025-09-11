turma1 = input ("Digite os nomes dos seus alunos:")
lista1 = turma1.split(",")
nomesComA = [nome for nome in lista1 if nome.startswith("A")]
print("Alunos que começam com A: ", nomesComA)