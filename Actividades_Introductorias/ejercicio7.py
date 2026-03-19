#Imprimir listas de palabras (ingresada por usuario) con +3 letras

lista_palabras = []

while True:
    palabra = input ('Ingrese una palabra: ')
    lista_palabras.append(palabra)
    if palabra == "FIN":
        break

lista_valida = []
for palabra in lista_palabras:
    if (len(palabra)<= 3):
        continue
    lista_valida.append(palabra)

print(lista_valida)
