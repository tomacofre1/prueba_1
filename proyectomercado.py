import os
while True:
    vendedor = input("Ingrese nombre del vendedor: ")
    producto = input("Ingrese producto: ")
    tipo = str.upper(input("Ingrese el tipo de producto: Ponga [L] para Lacteo / [B] para Bebestible / [N] para no perecible: "))
    cantidad = int(input("Ingrese la cantidad de productos: ")) 
    precio = int(input("Ingrese el precio del producto: "))

    if tipo == "L":
        tipo_prod = "Lacteo"
    elif tipo == "B":
        tipo_prod = "Bebestible"
    elif tipo == "N":
        tipo_prod = "No perecible"
    else:
        tipo_prod = "No existe"

    total_venta = cantidad * precio

    print(f"--------\nEl precio total es: ${total_venta}\nY el tipo de producto es {tipo_prod}\n--------")
    terminar = int(input("Si desea continuar presione 1: "))
    if terminar == 1:
        os.system("cls")
        
    else:
        print("Adios")
        break
    


