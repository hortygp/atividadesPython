import requests
from collections import Counter

def contarCoisas(entrada):
    if type(entrada)== type([]):
       contador = contaLista(entrada)
    else:
        contador = contaTexto(entrada)

    return contador

def contaLista(entrada):
    return Counter(entrada)

def contaTexto(entrada):
    return Counter(entrada.split())

#contador = contarCoisas([1,2,3,4,5,1,4,4,])
#contador = 0
#print(contador)
