def obtener_palabras(lista):
    palabras = lista[0].split(",")
    palabras_minusculas = []
    for pal in palabras:
       palabras_minusculas.append(pal.lower())
    return palabras_minusculas



def filtro (review,lista_palabras):
    filtrado_palabras = obtener_palabras(lista_palabras)
    palabras_review = review.split(" ")
    resultado = ""

    for palabra in palabras_review:
        if palabra.lower() in filtrado_palabras:
            resultado += "*"*len(palabra)+" "
        else:
            resultado += palabra + " "
    return resultado.strip()





