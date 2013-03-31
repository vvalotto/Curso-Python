'''
Created on 30/03/2013

@author: voval
'''

class Robot(object):
    '''
    Representa un robot, con un nombre.
    '''
    poblacion = 0

    def __init__(self, nombre):
        self.nombre = nombre
        print('Inicializando {0}'.format(self.nombre))
        
        Robot.poblacion += 1
    
    def __del__(self):
        print('{0} esta siendo destruido'.format(self.nombre))
        
        Robot.poblacion -= 1
        
        if Robot.poblacion == 0:
            print('{0} es el último.'.format(self.nombre))
        else:
            print('Todavia quedan {0:d} funcionado.'.format(self.poblacion))
    
    def decirHola(self):
        print('Saludos, me llamo {0}'.format(self.nombre))
        
    @staticmethod   
    def Cuantos():
        print('Somos {0:d} robots'.format(Robot.poblacion))
    

        
        