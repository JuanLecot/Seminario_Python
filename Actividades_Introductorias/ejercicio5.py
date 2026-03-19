# Caja Registradora: Ingreso Precios de a uno y Calculo Total

total= float(0)
precio = float (input("Ingrese el precio del producto: $"))
while precio != 0:
    if (precio == 0):
        break
    total+= precio
    precio = float(input("Ingrese precio de otro producto (0 para finalizar): $"))

print (f"Precio Total ${total:2}")

