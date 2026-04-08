# Juego del Ahorcado (Hangman Game)

Un juego del ahorcado interactivo desarrollado en Python con dos modos de juego: consola y GUI.

## Características

- **Modo Consola**: Interfaz de texto clásico
- **Modo GUI**: Interfaz visual estilo RETRO con temática de terminal
- 100 palabras relacionadas con programación
- Soporte para la letra Ñ

## Instalación

No requiere instalación adicional. Solo necesitas Python 3.6+.

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/juego-ahorcado.git
cd juego-ahorcado
```

## Uso

### Modo Consola

```bash
python ahorcado.py
```

### Modo GUI (Tkinter)

```bash
python gui_ahorcado.py
```

## Estructura del Proyecto

```
Juego del Ahorcado/
├── ahorcado.py          # Juego en modo consola
├── gui_ahorcado.py      # Juego con interfaz gráfica
├── logica_juego.py      # Lógica del juego (clase EstadoJuego)
├── estados_graficos.py  # Estados del ahorcado (ASCII art)
├── palabras.py          # Lista de 100 palabras de programación
├── README.md           # Este archivo
```

## Palabras Incluidas

El juego incluye 100 palabras relacionadas con programación como: python, java, algoritmo, función, clase, objeto, herencia, recursividad, api, docker, kubernetes, git, y muchas más.

## Licencia

MIT License
