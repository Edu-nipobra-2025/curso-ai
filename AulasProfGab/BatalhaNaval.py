import numpy as np

tabuleiro = np.array([
["#",".",".","S",".",".",".","."],
[".",".",".","#",".",".",".","."],
["#",".",".",".",".",".",".","."],
[".",".",".",".",".","#",".","."],
["#",".",".",".",".",".",".","#"],
[".",".",".",".",".",".",".","."],
[".",".","#",".",".",".","G","."]
[".",".",".","#",".",".",".","g"]])
inicio =(0,0)
objetivo = (6,7)

movimentos = [(-1,0),(1,0),(0,-1),(0,1)]

def BFS_Tabuleiro(tabuleiro, inicio, jogo):
    n, m = tabuleiro.shape
    lista = [inicio]
    visitados  = np.full([n,m], False)
    pais = np.full((n,m,2), -1)


    visitados [inicio] = True
    indice = 0
    passo = 0

    while indice < len(lista):
        x,y = lista[indice]
        indice = indice + 1

        if(x,y) == objetivo:
         caminho = []
         while (x,y) != (-1,-1):
          caminho.append((x,y))
          x,y = pais[x,y]
         return caminho, passo


        passo = passo + 1
        for dx, dy in movimentos:
            nx = x + dx
            ny =  y + dy
            if 0 <= nx < n and 0 <= ny < m and not visitados[nx, ny] and not "#":
                lista.append((nx,ny))
                visitados[nx,ny] = True
                pais[nx,ny] = (x,y)

caminho, passo = BFS_Tabuleiro(tabuleiro,inicio, objetivo)

for pos in caminho:
 print(pos)

print(passo)