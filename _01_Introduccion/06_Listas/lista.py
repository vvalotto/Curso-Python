'''
Created on 30/03/2013

@author: voval
'''

#Una lista es una estructura que mantiene una coleccion ordenada de elementos
#Es un tipo de datos mutable.

lista_super = ['cerveza', 'yoghurt', 'leche', 'pan']

print('Tengo que comprar ', len(lista_super), 'tipos de cosas')

print('Esas cosas son: ', end=' ')
for item in lista_super:
    print(item, end=', ')
    
print('Me acorde del arroz')
lista_super.append('arroz')
print('Ahora la lista es:', lista_super)

print('Ahora ordeno la lista')
lista_super.sort()
print('Mi lista ordenada:', lista_super)

print('El primer elemento de la lista es: ', lista_super[0])
compro_item = lista_super[0]
print('Compre: ', compro_item)
del lista_super[0]
print('Me queda por comprar :', lista_super)



    
