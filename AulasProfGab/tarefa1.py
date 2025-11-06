import numpy as np

xTreino = np.array([[1,0],[0,1],[0,0],[1,1]])
yTreino = np.array([[0],[0],[0],[1]])
def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_derivative(z):
    return z*(1-z)

np.random.seed(42)
pesos =- np.random.rand(1)
bias = np.random.rand(1)

taxaDeAprendizado = 0.1

for epoca in range (10):
    z = np.dot(bias,pesos) + bias
    yPredito = sigmoid(z)
    erro = yTreino - yPredito

    dW = np.dot (xTreino.T,erro *
                 sigmoid_derivative (yPredito))
    db = np.sum (xTreino.T,erro *
                 sigmoid_derivative (yPredito))
    
    pesos = pesos + taxaDeAprendizado * dW
    bias = bias + taxaDeAprendizado * db
    print (yPredito)