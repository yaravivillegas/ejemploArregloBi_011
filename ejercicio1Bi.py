'''
Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
con elementos aleatorios de números enteros del 0 al 100.
'''
import numpy as np
import random

matriz = np.diag([1,1,1]) #crear matriz 3x3 con diagonal con 1's
print(matriz)

#recorrer matriz
for i in range(3):
    for j in range(3):
        print(matriz[i][j])
        
#llenar con números aleatorios
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,100)
print(matriz)
        
        