'''
Created on 30/03/2013

@author: voval
'''
#Un diccionario es como una libro de direcciones, se indica un nombre y se obtienen los datos asociados

contactos = { "franco" : "paco@hotmail.com",
              "alejo" : "alejo@gmail.com",
              "cynthia" : "cfistra@gmai.com",
              "victor" : "vvalotto@gmail.com"}

print("El mail de franco es", contactos['franco'])

del contactos['victor']

print('\nhay {0} contactos la lista\n'.format(len(contactos)))

for nombre, email in contactos.items():
    print('Contact {0} at {1}'.format(nombre, email))
    
# Adding a key-value pair
contactos['otro'] = 'guido@python.org'

if 'otro' in contactos: # o ab.has_key('otro')
    print("\nOtro tiene el email:", contactos['otro'])
    