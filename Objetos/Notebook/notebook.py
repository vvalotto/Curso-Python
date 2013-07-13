'''
Created on 15/06/2013

@author: voval
'''

import datetime

#Guarda el proximo id disponible para todas las notas
last_id = 0

class Note:
    '''Representa una nota del Libro de Notas. Matchea contra
    una cadena para buscar y guarda etiquetas para cada nota.'''
    
    def __init__(self, memo, tags=''):
        '''Inicializa una nota con memo tags opcionales
        separados por coma. Automaticamente se pone el id
        y la fecha de creacipn'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def match(self,filter):
        '''Determina si la nota matchea con el filro de texto.'''
        
        return filter in self.memo or filter in self.tags
    
class Notebook:
    '''Representa una coleccion de notas que pueden ser etiquetadas,
    modificadas, y buscadas'''
    def __init__(self):
        '''Inicializa una lista vacia'''
        self.notes =[]
        
    def nueva_nota (self,memo,tags=''):
        '''Crea una nueva nota y la agrega a la lista'''
        self.notes.append(Note(memo,tags))

    def modificar_nota(self, note_id, memo):
        '''Encuentra una nota por el id y cambia su contenido con el memo nuevo'''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break
    
    def modificar_tags(self,note_id, tags):
        '''Encuentra una nota para un id dado y cambia las etiquetas'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
            
    def buscar(self, filter):
        '''Busca las notas que coinciden con la cadena del filro'''
        return [note for note in self.notes if note.match(filter)]
        