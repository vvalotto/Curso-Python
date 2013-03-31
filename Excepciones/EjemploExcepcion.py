'''
Created on 31/03/2013

@author: voval
'''

try:
    texto = input('Ingresar algo -->')
except EOFError:
    print('¿Porque abortaste el ingreso?')
except KeyboardInterrupt:
    print('Porque cancelaste?')
else:
    print('Ingresaste : {0}'.format(texto))