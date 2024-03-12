"""Aprender metodos de ordenamiento"""
from random import sample
import time
def burbuja(vector):
    size = len(vector)
    for i in range(size - 1):
        for j in range (0, size-1-i):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector



'''Ordenamineto de selescción'''
def seleccion (vector):
    for i in range(len(vector)-1):
        menor = i
        for j in range (i +1, len(vector)):
            if vector[j]< vector[menor]:
                menor = j
        if menor != i:
            vector[menor], vector[i] = vector[i], vector[menor]

'''Ordenamiento Shell '''
def shell (vector):
    size = len(vector)
    for i in vector:
        size += 1
    dist = size //2
    while dist>0:
        for i in range(dist, size):
            valor = vector[i]
            j=i
            while j >= dist and vector [j - dist] > valor :
                vector[j]= vector[j-dist]
                j -= dist
            vector[j]=valor
        dist //=2

lista = list(range(10000000))

vector = sample(lista, 1000)

start_time = time.time ()
burbuja(vector)
end_time = time.time()
print('El tiempo de ejecucion del metodo de burbuja es de: ', end_time - start_time)

start_time = time.time ()
seleccion(vector)
end_time = time.time()
print('El tiempo de ejecucion del metodo de seleccion es de: ', end_time - start_time)

start_time = time.time ()
shell(vector)
end_time = time.time()
print('El tiempo de ejecucion del metodo de shell es de: ', end_time - start_time)