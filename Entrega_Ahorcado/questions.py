import random

#Diccionario: Uso de Tuplas (clave = (codigo , nombre))
categorias_ahorcado = {
    (0,"Finalizar"): [],
    (1,"Lenguajes de programacion"): [
        "python", "java", "pascal", "javascript", "ruby", "kotlin"
    ],
    (2,"Fundamentos de programacion"): [
        "programa", "variable", "funcion", "bucle", "algoritmo", "sintaxis", "compilador"
    ],
    (3,"Tipos y estructuras de datos"): [
        "cadena", "entero", "lista", "booleano", "flotante", "diccionario", "tupla"
    ],
    (4,"Algoritmos avanzados"): [
        "dijkstra", "recursividad", "grafos", "busqueda", "ordenamiento"
    ],
    (5,"Desarrollo de software"): [
        "framework", "libreria", "repositorio", "interfaz", "depuracion", "api"
    ],
    (6,"Arquitectura de computadoras"): [
        "motherboard", "procesador", "registros", "cache", "transistores", "perifericos"
    ],
    (7,"Ramas de la matematica"): [
        "algebra", "calculo", "estadistica", "geometria", "aritmetica"
    ]
}


print("¡Bienvenido al Ahorcado!")

print()
print()
# Menu de Juego
while True:
    print ("--- MENU ---")
    print("+ Seleccione una de las siguientes categorias: ")
    for categoria in categorias_ahorcado:
        clave_numero = categoria[0]
        clave_nombre = categoria[1]
        print(f"{clave_numero} : {clave_nombre}")

    categoria_seleccionada = int(input("Seleccione el numero de categoria: "))

    if categoria_seleccionada == 0:
        print("Juego Finalizado.")
        break
    elif categoria_seleccionada>=1 and categoria_seleccionada<=7:
        #Busqueda Tupla Seleccionada
        tupla = ()
        for categoria in categorias_ahorcado:
            if categoria[0] == categoria_seleccionada:
                tupla = categoria
                break

        #Rondas y Nueva Lista
        rondas = int (input (f"Ingrese la cantidad de rondas a jugar (Maximo {len(categorias_ahorcado[tupla])}): "))
        palabras = random.sample(categorias_ahorcado[tupla],rondas)


        for i in range(len(palabras)):
            print()
            print(f"RONDA {i+1}")

            word = palabras[i]

            guessed = []
            attempts = 6
            puntaje = 0

            while attempts > 0:
                # Mostrar progreso: letras adivinadas y guiones para las que faltan
                progress = ""
                for letter in word:
                    if letter in guessed:
                        progress += letter + " "
                    else:
                        progress += "_ "
                print(progress)

                # Verificar si el jugador ya adivinó la palabra completa
                if "_" not in progress:
                    print ("-"*10)
                    print("¡Ganaste!")
                    puntaje += 6 #Puntaje x Ganar
                    break

                print(f"Intentos restantes: {attempts}")
                print(f"Letras usadas: {', '.join(guessed)}")

                letter = input("Ingresá una letra: ")
                
                if letter in guessed:
                    print("Ya usaste esa letra.")
                elif letter in word:
                    guessed.append(letter)
                    print("¡Bien! Esa letra está en la palabra.")
                
                # Caso Invalido: Caracter Especial, Numero o Palabra
                elif (letter < "a" or letter > "z") or (len(letter) > 1):
                    print ("Entrada No Valida.")

                else: 
                    guessed.append(letter)
                    attempts -= 1
                    print("Esa letra no está en la palabra.")
                    puntaje -= 1 

                print()
            else:
                print ("-"*10)
                print(f"¡Perdiste! La palabra era: {word}")
                puntaje = 0 # Puntaje x Perder

            print(f"Tu Puntaje es {puntaje}")
            print("-"*10)
    else:
        print()
        print("Opcion Invalida.")
        print()
