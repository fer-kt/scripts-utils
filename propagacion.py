# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:04:03 2021

@author: fernando
"""
# 0 = nuevo
# 1 = prendido
# -1 = quemado
#%%
def propagar(lista):
    temporal = [] # se guardan los segmentos entre los -1
    final = []
    for i, e in enumerate(lista):
        temporal.append(e) #se guarda el valor en la lista temporal
        if e == -1 or i == (len(lista)-1): #  si es -1 o el último elemento, recorre el segmento 
            if 1 in temporal: # si es que hay uno encendido en el segmento, debe encender los demas
                for t in temporal:
                    if t == 0:
                        final.append(1)
                    else:
                        final.append(t)
            else: # no hay ninguno encendido en el segmento, lo pasamos a la lista final tal cual está
                for t in temporal:
                    final.append(t)
            temporal= []
            

    return final

