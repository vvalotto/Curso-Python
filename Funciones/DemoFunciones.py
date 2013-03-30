'''
Created on 29/03/2013

@author: voval
'''

import Primos

Primos.ListarPrimos(2, 150)


num=193
print(num, ' es primo' if Primos.EsPrimo(num) else 'no es primo')
