def calculadora():
    print("=== Calculadora Simple ===")
    print("Operaciones: +  -  *  /")
    
    while True:
        num1 = float(input("\nIngresa el primer número: "))
        operacion = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                print("Error: no se puede dividir entre cero")
                continue
            resultado = num1 / num2
        else:
            print("Operación no válida")
            continue
        
        print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
        
        seguir = input("\n¿Quieres hacer otra operación? (s/n): ")
        if seguir.lower() != "s":
            print("¡Hasta luego!")
            break

calculadora()
