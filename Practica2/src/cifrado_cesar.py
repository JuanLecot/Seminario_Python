def cifrar_mensaje(mensaje,desplazamiento):
    mensaje_cifrado = ""
    letra_cifrada=""
    for letra in mensaje:
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            letra = chr ((ord(letra) - base + desplazamiento)% 26 + base)
        mensaje_cifrado +=letra
    return mensaje_cifrado