import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora 2")

        # Etiquetas
        etiqueta_valor1 = tk.Label(root, text="Valor 1:")
        etiqueta_valor1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        etiqueta_valor2 = tk.Label(root, text="Valor 2:")
        etiqueta_valor2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        etiqueta_resultado = tk.Label(root, text="Resultado:")
        etiqueta_resultado.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        etiqueta_operaciones = tk.Label(root, text="Operaciones:")
        etiqueta_operaciones.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # RadioButtons para las operaciones
        self.operacion_var = tk.StringVar()
        operacion_sumar = tk.Radiobutton(root, text="Sumar", variable=self.operacion_var, value="sumar")
        operacion_sumar.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        operacion_restar = tk.Radiobutton(root, text="Restar", variable=self.operacion_var, value="restar")
        operacion_restar.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        operacion_multiplicar = tk.Radiobutton(root, text="Multiplicar", variable=self.operacion_var, value="multiplicar")
        operacion_multiplicar.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        operacion_dividir = tk.Radiobutton(root, text="Dividir", variable=self.operacion_var, value="dividir")
        operacion_dividir.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        # LineEdits para los valores y el resultado
        self.valor1_entry = tk.Entry(root)
        self.valor1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.valor2_entry = tk.Entry(root)
        self.valor2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.resultado_entry = tk.Entry(root, state="readonly")
        self.resultado_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botón Calcular
        calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        calcular_button.grid(row=3, column=1, padx=10, pady=10)

    def calcular(self):
        valor1 = float(self.valor1_entry.get())
        valor2 = float(self.valor2_entry.get())
        operacion = self.operacion_var.get()

        if operacion == "sumar":
            resultado = valor1 + valor2
        elif operacion == "restar":
            resultado = valor1 - valor2
        elif operacion == "multiplicar":
            resultado = valor1 * valor2
        elif operacion == "dividir":
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return

        self.resultado_entry.config(state="normal")
        self.resultado_entry.delete(0, tk.END)
        self.resultado_entry.insert(0, str(resultado))
        self.resultado_entry.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
