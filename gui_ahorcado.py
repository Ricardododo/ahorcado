import tkinter as tk
from tkinter import font
from typing import Optional
from logica_juego import EstadoJuego, nuevo_juego
from estados_graficos import AHORCADO, MAX_INTENTOS


COLORES = {
    "bg": "#0d1117",
    "fg": "#00ff41",
    "fg_oscuro": "#008f11",
    "letra_correcta": "#00ff41",
    "letra_incorrecta": "#ff3333",
    "panel": "#161b22",
    "borde": "#30363d",
}


class InterfazAhorcado:
    def __init__(self, raiz: tk.Tk) -> None:
        self.raiz = raiz
        self.raiz.title("AHORCADO")
        self.raiz.configure(bg=COLORES["bg"])
        self.raiz.resizable(False, False)

        self.juego: Optional[EstadoJuego] = None
        self.botones_letras: dict[str, tk.Button] = {}

        self._crear_widgets()
        self._iniciar_juego()

    def _crear_widgets(self) -> None:
        fuente_titulo = font.Font(family="Courier New", size=24, weight="bold")
        fuente_palabra = font.Font(family="Courier New", size=32, weight="bold")
        fuente_normal = font.Font(family="Courier New", size=14)
        fuente_boton = font.Font(family="Courier New", size=12, weight="bold")

        titulo = tk.Label(
            self.raiz,
            text="=== AHORCADO RETRO ===",
            font=fuente_titulo,
            bg=COLORES["bg"],
            fg=COLORES["fg"]
        )
        titulo.pack(pady=(20, 10))

        self.frame_ahorcado = tk.Frame(self.raiz, bg=COLORES["bg"])
        self.frame_ahorcado.pack()

        self.canvas = tk.Canvas(
            self.frame_ahorcado,
            width=300,
            height=280,
            bg=COLORES["bg"],
            highlightthickness=0
        )
        self.canvas.pack(side=tk.LEFT, padx=(20, 10))

        self.frame_info = tk.Frame(self.frame_ahorcado, bg=COLORES["bg"])
        self.frame_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.label_palabra = tk.Label(
            self.frame_info,
            text="",
            font=fuente_palabra,
            bg=COLORES["bg"],
            fg=COLORES["fg"]
        )
        self.label_palabra.pack(pady=(30, 20))

        self.label_intentos = tk.Label(
            self.frame_info,
            text="",
            font=fuente_normal,
            bg=COLORES["bg"],
            fg=COLORES["fg_oscuro"]
        )
        self.label_intentos.pack()

        self.label_mensaje = tk.Label(
            self.frame_info,
            text="",
            font=fuente_normal,
            bg=COLORES["bg"],
            fg=COLORES["letra_incorrecta"]
        )
        self.label_mensaje.pack(pady=10)

        self.frame_teclado = tk.Frame(self.raiz, bg=COLORES["bg"])
        self.frame_teclado.pack(pady=20)

        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for i, letra in enumerate(letras):
            btn = tk.Button(
                self.frame_teclado,
                text=letra,
                font=fuente_boton,
                width=3,
                height=1,
                bg=COLORES["panel"],
                fg=COLORES["fg"],
                activebackground=COLORES["fg"],
                activeforeground=COLORES["bg"],
                relief=tk.FLAT,
                bd=2,
                command=lambda l=letra: self._adivinar(l)
            )
            btn.grid(row=i // 9, column=i % 9, padx=3, pady=3)
            self.botones_letras[letra] = btn

        self.frame_botones = tk.Frame(self.raiz, bg=COLORES["bg"])
        self.frame_botones.pack(pady=(0, 20))

        self.btn_nuevo = tk.Button(
            self.frame_botones,
            text="[NUEVO JUEGO]",
            font=fuente_boton,
            bg=COLORES["panel"],
            fg=COLORES["fg"],
            activebackground=COLORES["fg"],
            activeforeground=COLORES["bg"],
            relief=tk.FLAT,
            bd=2,
            command=self._iniciar_juego
        )
        self.btn_nuevo.pack(side=tk.LEFT, padx=10)

        self.btn_salir = tk.Button(
            self.frame_botones,
            text="[SALIR]",
            font=fuente_boton,
            bg=COLORES["panel"],
            fg=COLORES["fg"],
            activebackground=COLORES["fg"],
            activeforeground=COLORES["bg"],
            relief=tk.FLAT,
            bd=2,
            command=self.raiz.destroy
        )
        self.btn_salir.pack(side=tk.LEFT, padx=10)

    def _dibujar_ahorcado(self) -> None:
        self.canvas.delete("all")
        estado = self.juego.intentos_fallidos if self.juego else 0
        lines = AHORCADO[estado].strip().split("\n")
        y = 10
        for line in lines:
            self.canvas.create_text(10, y, anchor=tk.NW, text=line, fill=COLORES["fg"], font=("Courier New", 10))
            y += 18

    def _actualizar_pantalla(self) -> None:
        if not self.juego:
            return
        self._dibujar_ahorcado()
        self.label_palabra.config(text=self.juego.get_estado())
        restantes = MAX_INTENTOS - self.juego.intentos_fallidos
        self.label_intentos.config(text=f"Intentos: {restantes}")

    def _adivinar(self, letra: str) -> None:
        if not self.juego:
            return
        letra_minus = letra.lower()
        btn_key = letra.upper()
        self.botones_letras[btn_key].config(state=tk.DISABLED, bg=COLORES["borde"], fg=COLORES["fg_oscuro"])
        resultado = self.juego.adivinar_letra(letra_minus)
        self.label_mensaje.config(text="")
        self._actualizar_pantalla()
        if resultado is None:
            self.label_mensaje.config(text="¡Ya usaste esa letra!")
        elif not resultado:
            self.label_mensaje.config(text="¡Incorrecto!", fg=COLORES["letra_incorrecta"])
        else:
            self.label_mensaje.config(text="¡Correcto!", fg=COLORES["letra_correcta"])
        self.raiz.after(800, lambda: self.label_mensaje.config(text=""))
        self._verificar_fin()

    def _verificar_fin(self) -> None:
        if not self.juego:
            return
        if self.juego.esta_ganado():
            self._mostrar_mensaje_final("¡GANASTE!", COLORES["letra_correcta"])
            self._deshabilitar_teclado()
        elif self.juego.esta_perdido():
            self._mostrar_mensaje_final(f"PERDISTE: {self.juego.palabra_secreta}", COLORES["letra_incorrecta"])
            self._deshabilitar_teclado()

    def _mostrar_mensaje_final(self, texto: str, color: str) -> None:
        self.label_mensaje.config(text=texto, fg=color, font=font.Font(family="Courier New", size=18, weight="bold"))

    def _deshabilitar_teclado(self) -> None:
        for btn in self.botones_letras.values():
            btn.config(state=tk.DISABLED)

    def _iniciar_juego(self) -> None:
        self.juego = nuevo_juego()
        for btn in self.botones_letras.values():
            btn.config(state=tk.NORMAL, bg=COLORES["panel"], fg=COLORES["fg"])
        self.label_mensaje.config(text="", fg=COLORES["letra_incorrecta"])
        self._actualizar_pantalla()


def main() -> None:
    raiz = tk.Tk()
    InterfazAhorcado(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()