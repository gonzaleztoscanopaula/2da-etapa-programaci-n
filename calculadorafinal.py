import tkinter as tk
from tkinter import messagebox
import math

def realizar_operacion():
    try:
        expresion = pantalla.get()
        resultado = eval(expresion)
        resultado_label.config(text="Resultado: " + str(resultado))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def agregar_caracter(caracter):
    pantalla.insert(tk.END, caracter)

def borrar_caracter():
    pantalla.delete(len(pantalla.get()) - 1, tk.END)

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

def calcular_radicacion():
    try:
        num = float(pantalla.get())
        resultado = math.sqrt(num)
        resultado_label.config(text="Resultado: " + str(resultado))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calcular_potenciacion():
    try:
        expresion = pantalla.get()
        base, exponente = expresion.split("**")
        base = float(base)
        exponente = float(exponente)
        resultado = base ** exponente
        resultado_label.config(text="Resultado: " + str(resultado))
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def calcular_coseno():
    try:
        angulo = float(pantalla.get())
        resultado = math.cos(math.radians(angulo))
        resultado_label.config(text="Resultado: " + str(resultado))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.configure(bg="pink")  # Fondo rosa

# Crear elementos de la GUI
frame = tk.Frame(root, bg="pink")

# Pantalla
pantalla = tk.Entry(frame, font=("Arial", 20), bd=10, relief="ridge", justify="right")
pantalla.grid(row=0, column=0, columnspan=4)

# Botones numéricos y operaciones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (texto, fila, columna) in botones:
    if texto == "=":
        btn = tk.Button(frame, text=texto, font=("Arial", 16), relief="ridge", padx=20, pady=20, command=realizar_operacion)
    elif texto == "0":
        btn = tk.Button(frame, text=texto, font=("Arial", 16), relief="ridge", padx=20, pady=20, command=lambda t=texto: agregar_caracter(t))
    else:
        btn = tk.Button(frame, text=texto, font=("Arial", 16), relief="ridge", padx=20, pady=20, command=lambda t=texto: agregar_caracter(t))
    btn.grid(row=fila, column=columna, padx=2, pady=2)

# Botón de borrar y limpiar
borrar_btn = tk.Button(frame, text="Borrar", font=("Arial", 16), relief="ridge", padx=20, pady=20, command=borrar_caracter)
borrar_btn.grid(row=5, column=0, padx=2, pady=2)

limpiar_btn = tk.Button(frame, text="Limpiar", font=("Arial", 16), relief="ridge", padx=20, pady=20, command=limpiar_pantalla)
limpiar_btn.grid(row=5, column=1, padx=2, pady=2)

# Botones de funciones adicionales
radicacion_btn = tk.Button(frame, text="√", font=("Arial", 16), relief="ridge", padx=20, pady=20, command=calcular_radicacion)
radicacion_btn.grid(row=1, column=4, padx=2, pady=2)

potenciacion_btn = tk.Button(frame, text="**", font=("Arial", 16), relief="ridge", padx=20, pady=20, command=lambda: agregar_caracter("**"))
potenciacion_btn.grid(row=2, column=4, padx=2, pady=2)

coseno_btn = tk.Button(frame, text="cos", font=("Arial", 16), relief="ridge", padx=20, pady=20, command=calcular_coseno)
coseno_btn.grid(row=3, column=4, padx=2, pady=2)

# Etiqueta de resultado
resultado_label = tk.Label(frame, text="", font=("Arial", 16), bg="pink")
resultado_label.grid(row=6, column=0, columnspan=5)

# Colocar elementos en la ventana
frame.pack(padx=20, pady=20)

# Iniciar el ciclo principal de la GUI
root.mainloop()
