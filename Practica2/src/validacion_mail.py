def verificar_punto(cadena):
    for letra in cadena[-1::-1]:
        if letra == "@":
            return False
        if letra == ".":
            return True

def verificar_dominio(cadena):
    cadena = cadena.split(".")
    parte = cadena[-1]

    if (len(parte)>= 2):
        return True
    return False


def validar (mail):
    if mail.count("@")== 1:
        if (mail[0] != "@"):
            puntuacion = verificar_punto(mail)
            if puntuacion: 
                if not mail.endswith(("@",".")):
                    dominio = verificar_dominio(mail)
                    if dominio:
                        return True
    return False



    