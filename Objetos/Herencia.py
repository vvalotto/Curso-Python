'''
Created on 30/03/2013

@author: voval
'''

class MiembroComunidad():
    '''
    Representa un miembre de la comunidad academica
    '''


    def __init__(self, nombre, edad):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.edad = edad
        print('Miembro inicializado: {0}'.format(self.nombre))
        
    def mePresento(self):
        print('Nombre: "{0}" Edad:"{1}"'.format(self.nombre, self.edad))
    
    