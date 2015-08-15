'''
Created on 29/03/2013

@author: voval
'''

def ListarPrimos(minimo, maximo):
    for n in range(minimo, maximo):
        for x in range(minimo, n):
            if n % x == 0:
                print(n, ' es igual a ', x, '*' ,n//x)
                break
        else:
            print(n, ' Es un número primo')
            
def EsPrimo(numero):
    resultado = True
    for n in range(2, numero):
        if numero % n == 0:
            resultado = False
            break

    return resultado

