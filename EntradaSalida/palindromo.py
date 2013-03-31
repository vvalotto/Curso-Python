'''
Created on 31/03/2013

@author: voval
'''
#palindromo.py 

def inverso(texto):
    return texto[::-1]

def is_palindromo(texto):
    return texto == inverso(texto)

