'''
Created on 28/03/2013

@author: voval
'''
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test_spam"
    do_local()
    print("Despues del local:", spam)
    do_nonlocal()
    print('Despues del nonlocal:', spam)
    do_global()
    print('Despues del global:', spam)
    
scope_test()
print('Ambito global:', spam)