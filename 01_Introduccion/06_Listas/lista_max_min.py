
f = open("listanum")
lineas = f.readlines()
f.close()

fvalores = [float(linea) for linea in lineas]

print ("el maximo es {0}".format(max(fvalores)))
print ("el minimo es {0}".format(min(fvalores)))
