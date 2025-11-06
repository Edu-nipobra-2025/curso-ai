import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

dados = [16,47,16,20,15,19,20,20,18,16,19,15,15,16,18,18,15,19,18,14,17,19,17,17,17,17,16,14,17,24]

media = np.mean(dados)
mediana = np.median(dados)
moda = stats.mode(dados)
q1 = np.percentile(dados,25)
q2 = np.percentile(dados,50)
q3 = np.percentile(dados,75)
iqr = q3-q1

print(f"média: {media}")
print (f"mediana: {mediana}")
print(f"moda: {moda}")
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
plt.boxplot(dados, vert = False,patch_artist = True)
plt.title("Boxplot idades da turma")
plt.grid(True,linestyle = '--')
plt.show()