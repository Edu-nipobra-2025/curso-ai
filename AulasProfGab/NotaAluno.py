import numpy as np

x = np.array([
          [70, 8],
          [90,7],
          [85,6.5],
          [90,7.5],
          [50,7],
          [40,5],
          [80,6.5],
          [30,3],
          [80,4],
          [20,8]], dtype = float)

Y = np.array ([[0],[1],[1],[1],[0],[0],[1],[0],[0],[0]])

X = X/ np.max(X, axis=0)

np.random.seed(42)
pesos_camada_oculta = np.random.uniform(-1,1,(2,3))
pesos_saida = np.random.uniform(-1,1,(3,1))

taxa_aprendizado = 0.1

def sigmoid(X):
    return 1 / (1 + np.exp(-X))

def sigmoid_derivada(X):
    return X * (1 - X)

for epoca in range(100):
    camada_oculta = sigmoid(np.dot(X,pesos_camada_oculta))
    saida = sigmoid(np.dot(camada_oculta,pesos_saida))
    erro = Y- saida
    ajuste_saida = erro * sigmoid_derivada(saida)
    ajuste_oculta = ajuste_saida.dot(pesos_camada_oculta.T) * sigmoid_derivada(camada_oculta)
    
    pesos_saida += camada_oculta.T.dot(ajuste_saida) * taxa_aprendizado
    pesos_camada_oculta += X.T.dot(ajuste_oculta * taxa_aprendizado)

novo_aluno = np.array([70,6], dtype = float)
novo_aluno = novo_aluno / np.max(X, axis = 0)

camada_oculta = sigmoid(np.dot(novo_aluno, pesos_camada_oculta))
resultado = sigmoid(camada_oculta, pesos_camada_oculta)

resultado[0]