#Imprimir Numeros hasta N sin Multiplos de 5

numero = int(input("Ingrese un Numero: "))

for i in range(1, numero+1):
    if i % 5 == 0:
        continue
    print (i)

