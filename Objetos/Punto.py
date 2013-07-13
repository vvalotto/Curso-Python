
'''
Created on 13/06/2013

@author: voval
'''

import math

class Punto:
    'Representa un punto en coordenadas de dos dimensiones'
    
    def __init__(self, x=0, y=0):
        '''Inicializa la posicion de un nuevo punto. Las coordenada x e y
        pueden ser especificadas. Si no es asi el punto esta en el origen'''
        self.mover(x,y)
        
    def mover(self, x, y):
        '''Mueve el punto a una nueva posicion en dos dimensiones'''
        self.x = x
        self.y = y
        
    def inicio(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.mover(0, 0)
        
    def calcular_distancia(self, otro_punto):
        """Calculate the distance from this point to a second point
        passed as a parameter.
        
        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is returned
        as a float."""
        return math.sqrt(
                          (self.x - otro_punto.x)**2 +
                          (self.y - otro_punto.y)**2
                        )
        

                