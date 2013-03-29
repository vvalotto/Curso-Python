'''
Created on 29/03/2013

@author: voval
'''

#Estructura de Control Repetitivas; WHILE

numero = 23
en_ejecucion = True

while en_ejecucion:
    adivina = int(input('Ingrese un entero: '))
    
    if adivina == numero:
         print('Adivinaste!!!!')
         print('Sos un genio')
         en_ejecucion = False
    elif adivina < numero:
         print('Que fulero!!! le erraste por abajo')
    else:
         print('Mmmm!! me parece que te pasaste')
         
else:
    print('Fin de las adivinanzas')
         
print('Fin del programa')