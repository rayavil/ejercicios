# Muestra el tipo de angulo
#< 90 agudo,= 90 recto, > 90 y < 180 obtuso,= 180 llano,> 180 y < 360 concavo

import os
os.system("cls")

print("Muestra el tipo de angulo:\n")
angulo = int(input("Dame un angulo (o...360) :"))

if angulo >= 0  and angulo <= 360:
    print(f"El angulo es " , end= '')
    if angulo < 90:
        print("agudo")
    elif angulo == 90:
        print("Recto")
    elif angulo > 90 and angulo < 180:
        print("obtuso")
    elif angulo == 180:
        print ("llano")
    elif angulo > 180 and angulo < 360:
        print("Concavo")
    else:
        print("completo")

else:
    print("angulo fuera de rango...")

print("\n Proceso terminado")