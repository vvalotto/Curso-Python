'''
Created on 30/03/2013

@author: voval
'''
#|/usr/bin/env python
#Nombre: backup.py 

import os
import time

#1. Los archivos y directorios que seran respaldados son especificados en una Lista 

origen = ['/Users/voval/Documents/Temp', '/Users/voval/Documents/xampp']

#2. El backup sera guardado en un directorio ppal

dir_destino = '/Users/voval/Documents/backup'

#3.Los archivos son guardados en un archivo zip 
#4. El nombre del archivo es la hora y el dia actual

destino = dir_destino + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5. Usamos el comando zip para poner los archivos en un zip 
zip_comando = "zip -qr {0} {1}".format(destino, ' '.join(origen))

#Ejecutar el backup
print(zip_comando)
if os.system(zip_comando) == 0:
    print('Se hizo el backup en:', destino)
else:
    print('Fallo el backup')