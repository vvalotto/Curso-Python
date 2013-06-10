'''
Created on 09/06/2013

@author: voval
'''

def righ_justify(cadena):

    largo = len(cadena)
    cadenaDerecha =" "
    for i in range(1, (70 - largo)):
        cadenaDerecha = cadenaDerecha + " "
    return cadenaDerecha + cadena

print (righ_justify('HOLA'))
        
    
    