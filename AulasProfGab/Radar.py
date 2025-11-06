import numpy as np

tabuleiro = np.array([
    ["#", ".", ".", "S", ".", ".", ".", "."],
    [".", ".", ".", "#", ".", ".", ".", "."],
    ["#", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "#", ".", "."],
    ["#", ".", ".", ".", ".", ".", ".", "#"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", "G", "."],
    [".", ".", ".", "#", ".", ".", ".", "g"]
])

inicio = (4, 0)
objetivo = (6, 6)

movimentos = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

def Radar_Tabuleiro(tabuleiro, inicio, objetivo):
    n, m = tabuleiro.shape
    lista = [inicio]
    visitados = np.full((n, m), False)
    pais = np.full((n, m, 2), -1)

    visitados[inicio] = True
    indice = 0
    passo = 0

    while indice < len(lista):
        x, y = lista[indice]
        indice += 1

        if (x, y) == objetivo:
            caminho = []
            while (x, y) != (-1, -1):
                caminho.append((x, y))
                x, y = pais[x, y]
            caminho.reverse()
            return caminho, passo

        passo += 1

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visitados[nx, ny] and tabuleiro[nx, ny] != "#":
                lista.append((nx, ny))
                visitados[nx, ny] = True
                pais[nx, ny] = (x, y)

    return None, passo

caminho, passo = Radar_Tabuleiro(tabuleiro, inicio, objetivo)

if caminho:
    for pos in caminho:
        print(pos)
    print(f"Passos: {passo}")
else:
    print("Caminho não encontrado.")
