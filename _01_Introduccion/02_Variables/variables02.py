principal = 1000        # Monto inicial
tasa = 0.05             # Tasa de Interes
numanios = 5            # Numero de anios
anio = 1

while anio <= numanios:
    principal = principal * (1 + tasa)
    #salida formateada mejorada 2
    print(format(anio, "3d"), format(principal, "0.2f"))
    anio += 1
