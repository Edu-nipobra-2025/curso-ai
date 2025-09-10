a= input("Nomes na lista A (separados por vírgula):").strip()
b= input("Nomes na lista B (separados por vírgula):").strip()

lista_a = [x.strip() for x in a.split(",")if x.strip()]
lista_b = [x.strip() for x in b.split(",")if x.strip()]

listaUnida = lista_a + lista_b
vistos = set()
sem_dup = []

for nome in listaUnida:
    if nome.lower() not in vistos:
        sem_dup.append(nome)

print("Final (Ordenada)", sorted(sem_dup, key=str.casefold))