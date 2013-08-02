'''
Created on 14/07/2013

@author: voval
'''


class Color:

    def __init__(self, rgb_valor, nombre):
        '''
        Constructor
        '''
        self._rgb_valor = rgb_valor
        self._nombre = nombre
        
    def _set_nombre(self, nombre):
        if not nombre:
            raise Exception("Nombre Invalido")
        self._nombre = nombre
        
    def _get_nombre(self):
        return self._nombre
    
    nombre = property(_get_nombre, _set_nombre)