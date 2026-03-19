# Tablas De Multiplicar
RANGO = int(10)
numero = int (input("Ingrese un Numero: "))

print (f"TABLA DE MULTIPLICAR DE {numero}")
for i in range(1, RANGO + 1):
    print (f"{numero}*{i} = {numero*i}")
