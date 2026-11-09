import os



def menu():
    while True:
        print("\n---- CALCULADORA PONDERACIONES TEST 1.1 ----")
        
        print("\nPulsa 1 para calcular ponderacion notas")
        print(" ")
        print("Pulsa 2 para salir")
        opcion = input("ELIJA UNA OPCION: ")

        if opcion == "1":
            os.system('cls')
            calcular()
            print(" ")
            os.system("pause")
            os.system('cls')

           
        
        elif opcion == "2":
            os.system('cls')
            print("Hasta luego.")
            break

        else:
            os.system('cls')
            print("\n******PULSE UNA DE LAS TECLAS CORRECTAS PORFAVOR******")


def calcular():
    nota1 = float(input("Ingrese la PRIMERA nota sin coma (ejemplo: 40): "))
    ponde1 = int(input("Ingrese el porcentaje de ponderacion para la PRIMERA nota sin el '%' (ejemplo: 40 para 40%): "))
    os.system('cls')

    total1 = ponde1 / 100

    total_ponde = nota1 * total1

    nota2 = float(input("Ingrese la SEGUNDA nota sin coma (ejemplo: 40): "))
    ponde2 = int(input("Ingrese el porcentaje de ponderacion para la SEGUNDA nota sin el '%' (ejemplo: 40 para 40%): "))
    os.system('cls')

    total2 = ponde2 / 100

    total_ponde2 = nota2 * total2

    nota3 = float(input("Ingrese la TERCERA nota sin coma (ejemplo: 40): "))
    ponde3 = int(input("Ingrese el porcentaje de ponderacion para la TERCERA nota sin el '%' (ejemplo: 40 para 40%): "))
    os.system('cls')

    total3 = ponde3 / 100

    total_ponde3 = nota3 * total3

    nota4 = float(input("Ingrese la CUARTA nota sin coma (ejemplo: 40): "))
    ponde4 = int(input("Ingrese el porcentaje de ponderacion para la CUARTA nota sin el '%' (ejemplo: 40 para 40%): "))
   

    total4 = ponde4 / 100

    total_ponde4 = nota4 * total4

    total_total = total_ponde+total_ponde2+total_ponde3+total_ponde4

    os.system('cls')
    print(f"Las notas son   {int(nota1), int(nota2), int(nota3), int(nota4)}\nCon porcentajes ({ponde1}% {ponde2}% {ponde3}% {ponde4}%)\nY eso pondera -------> {total_total} ")

menu()

