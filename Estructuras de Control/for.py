'''
Created on 29/03/2013

@author: voval
'''

#Estructuras de control Repetitivas: FOR

print("Ejemplo 1: For simple")

for i in range(1,5):
    print(i)
else:
    print('FOR 1 finalizado')

#--------------------
for i in range(1,10,3):
     print("Indice :", i)

#--------------
lista = ['Victor', 'Cynthia', 'Franco', 'Alejo']
for item in lista:
    print(item)