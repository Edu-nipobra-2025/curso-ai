listaUm = []
listaDois = []
listaTotal = []
listaUmQuan = int(input("Digite uma quantia de números pra lista um:"))

listaDoisQuan = int(input("Digite uma quantia de números pra lista dois:"))
for _ in range (listaUmQuan):
    listaUm.append(float(input("número listaUm: ")))


for _ in range (listaDoisQuan):
  listaDois.append(float(input("número listaDois: ")))

listaTotal = [listaUm + listaDois]

print("Lista um quantia de numeros: ", listaUmQuan, "números: ", listaUm,"Lista dois quantia de numeros: ", listaDoisQuan, "números: ", listaDois, "Total: ", listaTotal )