'''
Created on 29/03/2013

@author: voval
'''

def valor(precio, iva=21, retencion=10):
    mi_monto = precio * ( 1 - iva/100)
    mi_retencion = mi_monto * (retencion/100)
    mi_factura = mi_monto - mi_retencion
    
    print('Me pagan: {0:5.2f}'.format(mi_factura))
    print('Me retienen: ', mi_retencion)
    print('Precio: ', precio, 'IVA: ', iva, 'Retencion:', retencion)
    
valor(100)
valor(100,retencion=12)
valor(iva=10.5, precio=200)