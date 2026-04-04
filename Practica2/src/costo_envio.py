ENVIO_LIVIANO = [500,1000,2000]
ENVIO_INTERMEDIO = [1000,2500,4500]
ENVIO_PESADO = [2000,5000,8000]

def envio_destino (destino,tipo_envio):
    match destino:
        case destino if destino == "local":
            return (tipo_envio[0])
        case destino if destino == "regional":
            return (tipo_envio[1])
        case destino if destino == "nacional":
            return (tipo_envio[2])
    return 0


def calcular_costo(peso,destino):
    zonas_validas = ["local","regional","nacional"]
    if destino not in zonas_validas:
        return "Zona no válida. Las zonas disponibles son: local, regional, nacional."

    match peso:
        case p if p <= 1:
            costo = envio_destino(destino,ENVIO_LIVIANO)
            return costo
        case p if p <= 5:
            costo = envio_destino(destino,ENVIO_INTERMEDIO)
            return costo
        case p if p > 5:
            costo = envio_destino(destino,ENVIO_PESADO)
            return costo
       
    return 0
