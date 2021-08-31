# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:00:10 2021

@author: fernando
"""

def invertir_lista(lista):
    nueva_lista = []
    i = len(lista)-1
    while i >= 0:
        nueva_lista.append(lista[i])
        i -= 1
    return nueva_lista

