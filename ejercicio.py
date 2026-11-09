#Se conoce los siguientes datos:
     #Nombre propietario
    # Tipo propiedad(C/D) Casa o departamento. Validar
   #  Acción a realizar (V/C) Venta o compra
  #   Monto de la propiedad
 # Se pide determinar:
#Impuesto a cancelar por el propietario de acuerdo a lo siguiente:
#Si es venta cancela un impuesto de un 10% del monto de la propiedad
#Si es compra cancela un impuesto de un 5% del monto de la propiedad

#Se pide  una vez ingresados lo datos del propietario, muestre por cada propietario
#Nombre propietario
#Tipo de propiedad en palabras
#Acción en palabras
#Monto de la propiedad
#Pago impuesto
#Al finalizar debe mostrar: Monto total de las propiedades / Nª de casas registradas / Nª de deptos. registrados

import os
while True:
    name = input("Ingrese nombre del propietario: ")
    while True:
        propi = str.upper(input("Ingrese tipo de propiedad [C]asa / [D]epto: "))
        if propi == "C":
            propie = "Casa"
            break
        elif propi == "D":
            propie = "Depto"
            break
        else:
            print("Porfavor ingresar tipo de propiedad correcto")
    while True:
        acci = str.upper(input("Ingrese accion a realizar [V]enta / [C]ompra: "))
        if acci == "V":
            accie = "Venta"
            break
        elif acci == "C":
            accie = "Compra"
            break
        else:
            print("Porfavor ingresar tipo de accion correcta")

    monto = int(input("Ingrese monto de la propiedad: "))
    if acci == "V":
        tax = 0.10
    elif acci == "C":
        tax = 0.05

    taxt = int(monto * tax)
    taxf = int(taxt + monto)

    print(f"-------------------\nEl nombre del propietario es: {name}\nEl tipo de propiedad es: {propie}\nLa accion a realizar sera: {accie}\nEl monto de la propiedad es de: ${monto}\nLos impuestos a pagar son: ${taxt}\nY el monto total a pagar con  impuestos seria: ${taxf}\n-------------------")

    seguir = int(input("Presione 1 para seguir: "))

    if seguir == 1:
        os.system("cls")
        

    else:
        break
 



