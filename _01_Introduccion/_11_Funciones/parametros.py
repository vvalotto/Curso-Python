def funcion (valor=10, *lista, **pares):
    print("El valor es: {0}".format(valor))
    print(lista[0])
    print(pares['dato'])


funcion(20, 1, 2, 8, dato=40, dato2=50)