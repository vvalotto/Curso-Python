'''
Created on 14/07/2013

@author: voval
'''

'1. Descomprimir archivo'
'2. Encontrar y reemplazar el texto'
'3. Comprimir archivo'

import sys, os, shutil, zipfile

class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(filename)
    
    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)