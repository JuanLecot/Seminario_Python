# Modificacion ejercicio 4, Armar Listas con Multiplos de 5 y Resto de Numeros 

lista_multiplos = []
lista_resto = []

numero = int(input("Ingrese un numero: "))

for i in range(1, numero+1):
    if i % 5 == 0:
        lista_multiplos.append(i)
    else:
        lista_resto.append(i)

print (f"{lista_multiplos}")
print (f"{lista_resto}")