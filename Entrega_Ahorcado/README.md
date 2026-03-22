  #Juego del Ahorcado
  - Lecot Juan Pedro 24313/7
---
  **funcionalidades**:
- Menu Continuo: Permite jugar multiples veces sin la necesidad de reiniciar el juego
- Categorias: 7 Categorias temáticas compuestas por una lista de palabras
- Sistema de Rondas: Eleccion de rondas a jugar, con limite segun la cantidad de palabras por categoria
- Puntuacion: Sistema de puntaje con penalizaciones por errores
- Validacion de Entrada: Maneja el ingreso de caracteres evitando errores por cadena de caracteres, caracteres especiales y/o numeros.

  **Consideraciones**
  Para la estructura del menu, decidi el uso de tuplas (codigo,nombre) permitiendo simplificar el menu interactivo pidiendo el ingreso de un numero en lugar
  de la cadena de caracteres.
  Implemente un bucle infinito que permita jugar multiples partidas en distintas categorias sin la necesidad de volver a ejecutar el programa desde consola cada vez,
  y utilizando la opcion de salida "0" que garantiza una finalizacion voluntaria.
  Limito la validacion del ingreso de letras al mismo formato de las palabras del jeugo, evitando problemas de case sensitivity.
