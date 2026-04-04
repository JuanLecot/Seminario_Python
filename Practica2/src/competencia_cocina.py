def ordenar_estadistica(estadisticas):
    #help(sorted)
    return sorted(estadisticas, key =lambda cocinero: estadisticas[cocinero]["Puntos"], reverse = True)


def procesar_ronda(ronda,estadisticas):
    max_cocinero = ""
    max_puntaje = -1

    for cocinero in ronda["scores"]:
        puntaje_cocinero_ronda = 0
        puntaje_cocinero_ronda = sum(nota for nota in ronda["scores"][cocinero].values())
        estadisticas[cocinero]["Puntos"]+=puntaje_cocinero_ronda

        if (estadisticas[cocinero]["Mejor Ronda"]) < puntaje_cocinero_ronda:
            estadisticas[cocinero]["Mejor Ronda"] = puntaje_cocinero_ronda

        if (puntaje_cocinero_ronda > max_puntaje):
            max_cocinero = cocinero
            max_puntaje = puntaje_cocinero_ronda
    
    ganador_ronda = (max_cocinero,max_puntaje)

    estadisticas[max_cocinero]["Rondas Ganadas"]+=1
    return ganador_ronda,estadisticas
        