'''
Created on 31/03/2013

@author: voval
'''

import pickle

lista_super_arch = 'lista.data'
lista_super = ['leche','pan','sal']

f = open(lista_super_arch, 'wb')
pickle.dump(lista_super, f)
f.close()

del lista_super

f = open(lista_super_arch, 'rb')
lista_super_copia = pickle.load(f)

for elemento in lista_super_copia:
    print(elemento)
