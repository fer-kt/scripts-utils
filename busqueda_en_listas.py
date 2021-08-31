# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:02:52 2021

@author: fernando
"""

def buscar_u_elemento(lista, e):
    '''reciba una lista y un elemento y devuelva la 
    posición de la última aparición de ese elemento en la 
    lista (o -1 si el elemento no pertenece a la lista)'''
    posicion = -1
    for indice, elemento in enumerate(lista):
        if elemento == e:
            posicion = indice
    return posicion
    
#%%

def buscar_n_elemento(lista, elemento):
    '''reciba una lista y un elemento
    y devuelva la cantidad de veces que aparece el
    elemento en la lista'''
    cantidad = 0
    for i in lista:
        if i == elemento:
            cantidad += 1
    return cantidad

#%%
def maximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

def minimo(lista):
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo

#%%

