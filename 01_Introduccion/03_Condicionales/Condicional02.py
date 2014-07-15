print("1 - .NET")
print("2 - Java")
print("3 - Python")

eleccion = int(input('Ingrese una opcion: '))

while True:
    if eleccion in [1, 2, 3]:
        break
    else:
        print("De nuevo, por favor")
        eleccion = int(input('Ingrese una opcion: '))

if eleccion == 1:
    print("Entity Framework")
elif eleccion == 2:
    print("Hibernate")
else:
    print("SqlAlchemy")



