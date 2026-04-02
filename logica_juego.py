from typing import Optional
from palabras import elegir_palabra


class EstadoJuego:
    """Estado del juego del ahorcado."""
    def __init__(self, palabra: str) -> None:
        self.palabra_secreta: str = palabra.lower()
        self.palabra_oculta: list[str] = ["_"] * len(self.palabra_secreta)
        self.letras_usadas: set[str] = set()
        self.intentos_fallidos: int = 0

    def adivinar_letra(self, letra: str) -> Optional[bool]:
        """Procesa un intento del jugador. Retorna True si acertó, False si falló, None si ya estaba usada."""
        letra = letra.lower()
        if letra in self.letras_usadas:
            return None
        
        self.letras_usadas.add(letra)
        
        if letra in self.palabra_secreta:
            for i, l in enumerate(self.palabra_secreta):
                if l == letra:
                    self.palabra_oculta[i] = letra
            return True
        else:
            self.intentos_fallidos += 1
            return False

    def esta_ganado(self) -> bool:
        """Verifica si el jugador ganó."""
        return "_" not in self.palabra_oculta

    def esta_perdido(self) -> bool:
        """Verifica si el jugador perdió."""
        from estados_graficos import MAX_INTENTOS
        return self.intentos_fallidos >= MAX_INTENTOS

    def get_estado(self) -> str:
        """Retorna el estado actual de la palabra."""
        return " ".join(self.palabra_oculta)


def nuevo_juego() -> EstadoJuego:
    """Inicia un nuevo juego."""
    palabra = elegir_palabra().lower()
    return EstadoJuego(palabra)