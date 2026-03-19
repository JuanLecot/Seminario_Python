# Caja Registradora: Ingreso Precios de a uno y Calculo Total

total_caja = float(0)

#Bucle INFINITO
while True:
    precio = float (input("Ingrese el precio del Producto: $"))

    if (precio == 0): #CORTE 
        break

    total_caja += precio

print(f"El total de la es de ${total_caja:2}")
