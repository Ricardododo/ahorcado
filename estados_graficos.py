AHORCADO = [
    """
    +---+
        |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|\ |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|\\|
    / \\|
        |
    =========
    """
]

MAX_INTENTOS = len(AHORCADO) - 1

def mostrar_estado(intentos_fallidos, palabra_oculta, letras_usadas):
    """Imprime el estado actual del juego."""
    print(AHORCADO[intentos_fallidos])
    print("\nPalabra: " + " ".join(palabra_oculta))
    print(f"Letras usadas: {', '.join(sorted(letras_usadas))}")
    print(f"Intentos restantes: {MAX_INTENTOS - intentos_fallidos}")