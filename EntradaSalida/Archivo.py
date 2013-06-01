'''
Created on 31/03/2013

@author: voval
'''

poema = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
     use Python!
'''
f = open('poema.txt','w') #Abrir el archivo para escribir
f.write(poema)
f.close()

f = open('poema.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()


