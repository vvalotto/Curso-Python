'''
Created on 30/03/2013

@author: voval
'''

class Persona():
    '''
    Clase que no hace nada
    '''
    def __init__(self, nombre):
        self.nombre = nombre
    
    def decirHola(self):
        print('Hola, compo estas?', self.nombre)
        
p = Persona('Alejo')
p.decirHola()



