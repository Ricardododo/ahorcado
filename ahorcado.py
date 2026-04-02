
import random
from palabras import elegir_palabra
from estados_graficos import mostrar_estado, MAX_INTENTOS

def jugar():
    palabra_secreta = elegir_palabra().lower()
    palabra_oculta = ["_"] * len(palabra_secreta)
    letras_usadas = set()
    intentos_fallidos = 0


    while True:
        mostrar_estado(intentos_fallidos, palabra_oculta, letras_usadas)

        #entrada del usuario
        entrada = input("Adivina una letra: ").lower().strip()
        if not entrada or len(entrada) != 1 or not entrada.isalpha():
            print("Entrada inválida. Por favor, ingresa una sola letra.\n")
            continue

        if entrada in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.\n")
            continue

        letras_usadas.add(entrada)

        if entrada in palabra_secreta:
            for i, letra in enumerate(palabra_secreta):
                if letra == entrada:
                    palabra_oculta[i] = letra
            print("¡Correcto! La letra está en la palabra\n")
        else:
            intentos_fallidos += 1
            print("¡Incorrecto! La letra no está en la palabra\n")
        
        if "_" not in palabra_oculta:
            mostrar_estado(intentos_fallidos, palabra_oculta, letras_usadas)
            print("¡Felicidades! Has adivinado la palabra secreta.")
            return True
        
        if intentos_fallidos == MAX_INTENTOS:
            mostrar_estado(intentos_fallidos, palabra_oculta, letras_usadas)
            print(f"¡Has perdido! La palabra secreta era: {palabra_secreta}")
            return False
        
def main():
    print("¡Bienvenido al juego del Ahorcado!")
    while True:
        jugar()
        if input("¿Quieres jugar de nuevo? (s/n): ").lower() != "s":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()