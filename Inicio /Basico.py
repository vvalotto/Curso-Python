'''
Created on 28/03/2013

@author: Victor Valotto
'''
#!/usr/bin/env python

import os

#Aspectos básicos del lenguaje

"""->Literales:
Es un elemento que se usa con el valor que se describe en el programa.'
Ejemplos:
"""
print("Ejemplo de Literales:")
print('1. Esta es una cadena (String) literal')
print('2. Este son números literales:')
print('2.a Entero', 5)
print('2.b Punto Flotante', 3.23, 45E-7)
print('2.c Números complejos', 4 + 7j)
#x = input('>')
#os.system('clear')

"String: secuencia de caracteres"

"Ejemplo de comentario con multiples lineas"
print('Muliples Lineas')
print('''Estes es un ejemplo con multiples lineas.
Esta es la segunda linea.
Estamos iniciando el curso''')

"Otra manera con secuencia de escapes"
print('Estes es un ejemplo con multiples lineas.\nEsta es la segunda linea.\nEstamos iniciando el curso''')
print('Una Columna\tDos Columnas')

"Concatenación de cadenas"
print('Mi nombre es: ' 'Victor')

"Formateo de la salida"
edad = 4
hijo = 'Alejo'
print('{0} tiene {1} años de edad'.format(hijo, edad))
print('Otros ejemplos')
print('{0:.3}'.format(1/3)) #Punto flotante con tres decimales
print('{0:_^11}'.format('Python')) #Llena con guiones bajos con el texto centrado con 11 caracteres de ancho
print('{nombre} creo {lenguaje}'.format(nombre='Guido von Rossum', lenguaje='Python'))