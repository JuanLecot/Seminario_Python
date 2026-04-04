def contar_lineas(texto):
    return len(texto.split("\n"))

def contar_palabras(texto):
    return len(texto.split())

def palabras_promedio (lineas,palabras):
    return palabras/lineas

def lineas_mayor_promedio(texto,promedio):
    lineas = texto.split("\n")
    for linea in lineas:
        palabras = linea.split()
        if (len(palabras)>promedio):
            print (f"{linea} ({len(palabras)} palabras)")

        
