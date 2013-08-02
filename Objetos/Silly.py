'''
Created on 14/07/2013

@author: voval
'''

class Silly:
    @property
    def silly(self):
        "Esta es una propiedad Silly"
        print("Estas obteniendo silly")
        return self._silly
    
    @silly.setter
    def silly(self, value):
        print("Estas poniendo {}".format(value))
        self._silly = value
    
    @silly.deleter
    def silly(self):
        print("Ooo, estas matando a silly")
        del self._silly
        