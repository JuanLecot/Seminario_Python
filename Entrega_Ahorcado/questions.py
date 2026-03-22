import random

#Diccionario 
categorias_ahorcado = {
    "Lenguajes de programacion": [
        "python", "java", "pascal", "javascript", "ruby", "c++"
    ],
    "Fundamentos de programacion": [
        "programa", "variable", "funcion", "bucle", "algoritmo", "sintaxis", "compilador"
    ],
    "Tipos y estructuras de datos": [
        "cadena", "entero", "lista", "booleano", "flotante", "diccionario", "tupla"
    ],
    "Algoritmos avanzados": [
        "dijkstra", "recursividad", "grafos", "busqueda", "ordenamiento"
    ],
    "Desarrollo de software": [
        "framework", "libreria", "repositorio", "interfaz", "depuracion", "api"
    ],
    "Arquitectura de computadoras": [
        "motherboard", "procesador", "registros", "cache", "transistores", "perifericos"
    ],
    "Ramas de la matemática": [
        "algebra", "calculo", "estadistica", "geometria", "aritmetica"
    ]
}

guessed = []
attempts = 6
puntaje = int(0)

print("¡Bienvenido al Ahorcado!")
print()

print()
print ("--- MENU ---")
print("+ Seleccione una de las siguientes categorias: ")

for categoria in categorias_ahorcado:
    print (f"- {categoria}")
categoria_seleccionada = input("Ingrese la categoria: ")

word = random.choice(categorias_ahorcado[categoria_seleccionada])

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
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0 # Puntaje x Perder

print(f"El Puntaje es {puntaje}")
