#Archivo que contiene lineas de la forma "nombre, lineas, autor"
archivo = "sistema.csv"
sistema = []
for linea in open(archivo):
    campos = linea.split(",")
    nombre = campos[0]
    lineascodigo = int(campos[1])
    autor = campos[2]
    programa = (nombre, lineascodigo, autor)
    sistema.append(programa)

print(sistema)