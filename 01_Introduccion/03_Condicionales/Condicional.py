
#Estructura de Control Condicional; IF

numero = 23
adivina = int(input('Ingrese un entero: '))

if adivina == numero:
     print('Adivinaste!!!!')
     print('Sos un genio')
elif adivina < numero:
     print('Que fulero!!! le erraste por abajo')
else:
     print('Mmmm!! me parece que te pasaste')
     
print('Fin!!')