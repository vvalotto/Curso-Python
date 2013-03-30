'''
Created on 29/03/2013

@author: voval
'''

import sys

print('Los arggumentos de la linea de comandos son:')
for i in sys.argv:
    print(i)

print('\n\nLa PYTHONPATH es ', sys.path, '\n')