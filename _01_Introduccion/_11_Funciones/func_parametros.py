'''
Created on 29/03/2013

@author: voval
'''

'''
Funcion 3 - Parametros
'''

def total(inicial=5, *numeros, **claves):
    cuenta = inicial
    print(cuenta)
    for numero in numeros:
        cuenta += numero
    print(cuenta)
    for clave in claves:
        cuenta += claves[clave]
        print(cuenta)
    return cuenta

print(total(10, 1, 2, 3, vegetales=50, frutas=100))
    
        