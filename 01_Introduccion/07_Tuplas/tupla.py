'''
Created on 30/03/2013

@author: voval
'''
#Las tuplas son usadas para mantener objetos multiples
#Son inmutables
from test.test_iterlen import len


zoo = ('leon', 'elefante', 'jirafa')
print('Numero de animales en el zoo:', len(zoo))

nuevo_zoo = ('mono','tigre',zoo)

print('Numero de jaulas', len(nuevo_zoo))
print('Estos son los animales del nuevo zoo', nuevo_zoo)