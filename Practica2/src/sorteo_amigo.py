import random

def realizar_sorteo (lista_nombres = list):
    
    participantes = [p.strip() for p in lista_nombres.split(",") if p.strip()]

    if len(set(p.lower() for p in participantes)) != len(participantes):
        print("Error: No debe haber nombres duplicados.")
        return

    if len(participantes) < 3:
        print("Error: Debe haber al menos 3 participantes.")
        return
    
    asignados = participantes[:]
    lista_sorteo = []
    valido = False
    while not valido:
        random.shuffle(asignados)
        valido = True
        for i in range(len(participantes)):
            if participantes[i] == asignados[i]:
                valido = False
                break

    for i in range(len(participantes)):
        lista_sorteo.append ((participantes[i],asignados[i]))
       
    return lista_sorteo


