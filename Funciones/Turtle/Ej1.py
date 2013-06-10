'''
Created on 09/06/2013

@author: voval
'''

from TurtleWorld import *

def cuadrado(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)
        
world = TurtleWorld()
bob = Turtle()
cuadrado(bob,200)
wait_for_user()
