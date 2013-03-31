'''
Created on 31/03/2013

@author: voval
'''

from palindromo import is_palindromo

def muestra_resultado(texto):
    if (is_palindromo(texto)):
        print('Si, es un palindromo')
    else:
        print('No, no es un palindromo')