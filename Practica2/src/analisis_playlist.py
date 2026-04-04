def obtener_tiempo(tiempo):
    lista_tiempo = tiempo.split(":")
    return (int(lista_tiempo[0])),(int(lista_tiempo[1]))


def obtener_duracion_playlist(playlist):
    total_sec = 0
    for cancion in playlist:
        minutos,segundos = obtener_tiempo(cancion["duration"])
        total_sec += (minutos*60)+segundos

    if (total_sec != 0):
        return (total_sec // 60) + (total_sec % 60)/100
 

def obtener_maximo(playlist):
    lista = []
    for cancion in playlist:
        minutos,segundos = obtener_tiempo(cancion["duration"])
        tiempo_total = minutos + (segundos)/100
        lista.append((tiempo_total,cancion["title"]))
    
    return max(lista)

def obtener_minimo(playlist):
    lista = []
    for cancion in playlist:
        minutos,segundos = obtener_tiempo(cancion["duration"])
        tiempo_total = minutos + (segundos)/100
        lista.append((tiempo_total,cancion["title"]))
    
    return min(lista)



    