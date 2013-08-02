'''
Created on 13/07/2013

@author: voval
'''

''' Problema: escribir un funcion que acepta cualquier numero de argumentos.'''

def promedio(primero, *resto):

    return (primero + sum(resto)) / (1 + len(resto))







#Ejemplo

print(promedio(1,2))

print(promedio(1,2,3,4))