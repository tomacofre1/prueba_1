#Programa con 3 notas, promedio y muestre el resultado

#notas
nota_1 = float(input("Ingresar nota N°1: "))
nota_2 = float(input("Ingresar nota N°2: "))
nota_3 = float(input("Ingresar nota N°3: "))

#calcular promedio
promedio = (nota_1 + nota_2 + nota_3) / 3

#mostrar promedio
print(f"El promedio de las 3 notas es: {promedio:.1f}")

#averiguar si el estudiante aprueba o  reprueba

if promedio >= 4.0:
    print("Felicidades! Aprobaste!")
else:
    print("Acabas de reprobar, hay que estudiar mas")