"""  RAMÓN ÁVILA GARCÍA
     COMPUTACIÓN APLICADA
     PRIMER  PARCIAL
     
Descripción: Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo
de usuario, paquete y cantidad.
• Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
• Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900
Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete,
y multiplicando por la cantidad solicitada.
Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente
• Es Alumno 20%
• Es Trabajador y un 10%
• Es Docente y un 5%
Al final mostrar un resumen con los datos calculados de la venta """

import os

importe_total = 0

while(True):

    t_usuario = int(input('Indique el tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500: '))

    paquete = int(input('Indica el paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900: '))

    cantidad = int(input('Cantidad dolicitada: '))

    print('\nTu pedido fue:')
    print('_'*100)
    v_usuario = 0
    v_paquete = 0
    v_cantidad = 0
    if t_usuario == 1:
        v_usuario = 100
        des_usuario ="Alumno" 
        

    if t_usuario == 2:
        v_usuario = 200
        des_usuario ="Trabajador" 
    
    if t_usuario == 3:
        v_usuario = 500
        des_usuario ="Docente" 

    if paquete == 1:
        v_paquete =600
        des_paquete = "Solo conferencias"

    if paquete == 2:
        v_paquete =800 
        des_paquete = "Con eventos sociales"

    
    if paquete == 3:
        v_paquete =900
        des_paquete = "Con kit de acceso"

    if paquete == 0 or t_usuario ==0:
        print('No seleccionaste un valor para tipo de usuario o de paquete valido.')
        res=input('\nDeseas continuar S/N?')
        if res.upper()=='N':
            break

    s_total= (v_usuario + v_paquete)*cantidad  
   

    #verificamos en que condición se encuentra el subtotal y el tipo de usuario
    if s_total > 5000 and t_usuario == 1 :
        v_descuento = (s_total *0.25)
        total =  s_total - v_descuento
        descuento = "25%"
    
    if s_total > 5000 and t_usuario == 2 :
        v_descuento = (s_total *0.10)
        total =  s_total - v_descuento
        descuento = "10%"

    if s_total > 5000 and t_usuario == 3 :
        v_descuento = (s_total *0.05)
        total =  s_total - v_descuento
        descuento = "5%"

    if s_total <= 5000 :
        v_descuento = 0
        total = s_total 
        descuento = "No tienes descuento porque el subtotal no es mayor 5,000.00 :( "


    importe_total = importe_total + total

    print ('Boletos: %s, Tipo de Usuario: %s, Tipo de paquete: %s' % (cantidad, des_usuario, des_paquete))
 

    print ('Subtotal: %s,  con un descuento de: %s (%s), El TOTAL es: %s' % (s_total, v_descuento, descuento, total) )


    res=input('\nDeseas continuar S/N?')
    if res.upper()=='N':
        print('-'*50)
        print ('|  El importe total de todos los accesos es: %s  ' % (importe_total))
        print('-'*50)
        break
