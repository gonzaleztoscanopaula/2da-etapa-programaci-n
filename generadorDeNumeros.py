import tkinter as tk
from tkinter import Label, Spinbox, Entry, Button

class GeneradorNumerosApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Generador de Números")
        self.raiz.geometry("400x300")

        self.configurar_interfaz()

    def configurar_interfaz(self):
        etiqueta_numero1 = Label(self.raiz, text="Primer Número:")
        self.entrada_numero1 = Spinbox(self.raiz, from_=0, to=100)

        etiqueta_numero2 = Label(self.raiz, text="Segundo Número:")
        self.entrada_numero2 = Spinbox(self.raiz, from_=0, to=100)

        etiqueta_numero_generado = Label(self.raiz, text="Número Generado:")
        self.entrada_numero_generado = Entry(self.raiz, state="readonly")

        boton_generar = Button(self.raiz, text="Generar", command=self.generar_numero)

        etiqueta_numero1.pack()
        self.entrada_numero1.pack()
        etiqueta_numero2.pack()
        self.entrada_numero2.pack()
        etiqueta_numero_generado.pack()
        self.entrada_numero_generado.pack()
        boton_generar.pack()

    def generar_numero(self):
        valor_minimo = int(self.entrada_numero1.get())
        valor_maximo = int(self.entrada_numero2.get())

        if valor_minimo > valor_maximo:
            valor_minimo, valor_maximo = valor_maximo, valor_minimo

        numero_generado = str(random.randint(valor_minimo, valor_maximo))
        self.entrada_numero_generado.config(state="normal")
        self.entrada_numero_generado.delete(0, tk.END)
        self.entrada_numero_generado.insert(0, numero_generado)
        self.entrada_numero_generado.config(state="readonly")

if __name__ == "__main__":
    import random

    raiz = tk.Tk()
    app = GeneradorNumerosApp(raiz)
    raiz.mainloop()
