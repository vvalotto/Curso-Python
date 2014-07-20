'''
Created on 29/03/2013

@author: voval
'''

def func_externa():
    x = 2
    print('x es : ', x)
    
    def func_interna():
        nonlocal x
        x = 5
        
    func_interna()
    print('x vale ahora: ', x)
    
func_externa()