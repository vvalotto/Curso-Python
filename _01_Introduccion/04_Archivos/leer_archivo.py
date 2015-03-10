#Lectura de un archivo

f = open("nombres")
linea = f.readline()
while linea:
    print(linea, end='')
    linea = f.readline()
f.close()