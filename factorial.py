import tkinter as tk
import math

def calcular_factorial():
    try:
        numero = int(entrada_n.get())
        factorial = math.factorial(numero)
        entrada_factorial.config(state="normal")
        entrada_factorial.delete(0, tk.END)
        entrada_factorial.insert(0, str(factorial))
        entrada_factorial.config(state="readonly")
    except ValueError:
        entrada_factorial.config(state="normal")
        entrada_factorial.delete(0, tk.END)
        entrada_factorial.insert(0, "Ingrese un número válido")
        entrada_factorial.config(state="readonly")

def siguiente():
    numero_actual = int(entrada_n.get()) + 1
    entrada_n.delete(0, tk.END)
    entrada_n.insert(0, str(numero_actual))
    entrada_factorial.config(state="normal")
    entrada_factorial.delete(0, tk.END)
    entrada_factorial.config(state="readonly")
    resultado_label.config(text="")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Factoriales")
ventana.configure(bg="pink")  # Fondo rosa
ventana.geometry("400x250")  # Tamaño de la ventana

# Crear elementos
etiqueta_n = tk.Label(ventana, text="n:", bg="pink")
etiqueta_n.pack()

entrada_n = tk.Entry(ventana)
entrada_n.pack()

etiqueta_factorial = tk.Label(ventana, text="Factorial (n):", bg="pink")
etiqueta_factorial.pack()

entrada_factorial = tk.Entry(ventana, state="readonly")
entrada_factorial.pack()

calcular_btn = tk.Button(ventana, text="Calcular Factorial", command=calcular_factorial)
calcular_btn.pack()

resultado_label = tk.Label(ventana, text="", font=("Arial", 12), bg="pink")
resultado_label.pack()

siguiente_btn = tk.Button(ventana, text="Siguiente", command=siguiente)
siguiente_btn.pack()

# Configuración inicial
numero_inicial = 1
entrada_n.insert(0, str(numero_inicial))

# Iniciar el ciclo principal de la GUI
ventana.mainloop()
