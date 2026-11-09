


nota1 = float(input("Ingrese la primera nota sin coma (ejemplo: 40 para un 4.0): "))
ponder = float(input("Que porcentaje pondera esa nota (ejemplo: 30% pero solo escriba 30): "))

total = ponder / 100

total_ponder = nota1 * total

nota2 = float(input("Ingrese la segunda nota sin coma (ejemplo: 40 para un 4.0): "))
ponder2 = float(input("Que porcentaje pondera esa nota (ejemplo: 30% pero solo escriba 30): "))

total2 = ponder2 / 100

total_ponder2 = nota2 * total2

nota3 = float(input("Ingrese la tercera nota sin coma (ejemplo: 40 para un 4.0): "))
ponder3 = float(input("Que porcentaje pondera esa nota (ejemplo: 30% pero solo escriba 30): "))

total3 = ponder3 / 100

total_ponder3 = nota3 * total3

nota4 = float(input("Ingrese la cuarta nota sin coma (ejemplo: 40 para un 4.0): "))
ponder4 = float(input("Que porcentaje pondera esa nota (ejemplo: 30% pero solo escriba 30): "))

total4 = ponder4 / 100

total_ponder4 = nota4 * total4

total_total = total_ponder + total_ponder2 + total_ponder3 + total_ponder4

print(f"Las notas son {nota1, nota2, nota3, nota4} y pondera un{total_total}")

