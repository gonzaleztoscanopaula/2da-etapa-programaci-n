import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora")
        self.raiz.configure(bg="pink") 

        self.primer_numero_label = tk.Label(raiz, text="Primer número:", bg="pink")
        self.primer_numero_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.primer_numero_entry = tk.Entry(raiz)
        self.primer_numero_entry.grid(row=0, column=1, padx=10, pady=10)

        self.segundo_numero_label = tk.Label(raiz, text="Segundo número:", bg="pink")
        self.segundo_numero_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.segundo_numero_entry = tk.Entry(raiz)
        self.segundo_numero_entry.grid(row=1, column=1, padx=10, pady=10)

        self.botones_frame = tk.Frame(raiz, bg="pink")
        self.botones_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.suma_button = tk.Button(self.botones_frame, text="+", command=self.sumar, width=5)
        self.suma_button.grid(row=0, column=0, padx=5, pady=5)

        self.resta_button = tk.Button(self.botones_frame, text="-", command=self.restar, width=5)
        self.resta_button.grid(row=0, column=1, padx=5, pady=5)

        self.multiplicacion_button = tk.Button(self.botones_frame, text="*", command=self.multiplicar, width=5)
        self.multiplicacion_button.grid(row=1, column=0, padx=5, pady=5)

        self.division_button = tk.Button(self.botones_frame, text="/", command=self.dividir, width=5)
        self.division_button.grid(row=1, column=1, padx=5, pady=5)

        self.porcentaje_button = tk.Button(self.botones_frame, text="%", command=self.porcentaje, width=5)
        self.porcentaje_button.grid(row=2, column=0, padx=5, pady=5)

        self.reset_button = tk.Button(self.botones_frame, text="RESET", command=self.reset, width=5)
        self.reset_button.grid(row=2, column=1, padx=5, pady=5)

        self.resultado_label = tk.Label(raiz, text="Resultado:", bg="pink")
        self.resultado_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.resultado_entry = tk.Entry(raiz, state="readonly")
        self.resultado_entry.grid(row=3, column=1, padx=10, pady=10)

    def verificar_numeros(self, num1, num2):
        try:
            float(num1)
            float(num2)
            return True
        except ValueError:
            return False

    def sumar(self):
        num1 = self.primer_numero_entry.get()
        num2 = self.segundo_numero_entry.get()
        if self.verificar_numeros(num1, num2):
            resultado = float(num1) + float(num2)
            self.resultado_entry.config(state="normal")
            self.resultado_entry.delete(0, tk.END)
            self.resultado_entry.insert(0, str(resultado))
            self.resultado_entry.config(state="readonly")
        else:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")

    def restar(self):
        num1 = self.primer_numero_entry.get()
        num2 = self.segundo_numero_entry.get()
        if self.verificar_numeros(num1, num2):
            resultado = float(num1) - float(num2)
            self.resultado_entry.config(state="normal")
            self.resultado_entry.delete(0, tk.END)
            self.resultado_entry.insert(0, str(resultado))
            self.resultado_entry.config(state="readonly")
        else:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")

    def multiplicar(self):
        num1 = self.primer_numero_entry.get()
        num2 = self.segundo_numero_entry.get()
        if self.verificar_numeros(num1, num2):
            resultado = float(num1) * float(num2)
            self.resultado_entry.config(state="normal")
            self.resultado_entry.delete(0, tk.END)
            self.resultado_entry.insert(0, str(resultado))
            self.resultado_entry.config(state="readonly")
        else:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")

    def dividir(self):
        num1 = self.primer_numero_entry.get()
        num2 = self.segundo_numero_entry.get()
        if self.verificar_numeros(num1, num2):
            if float(num2) != 0:
                resultado = float(num1) / float(num2)
                self.resultado_entry.config(state="normal")
                self.resultado_entry.delete(0, tk.END)
                self.resultado_entry.insert(0, str(resultado))
                self.resultado_entry.config(state="readonly")
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")
        else:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")

    def porcentaje(self):
        num1 = self.primer_numero_entry.get()
        num2 = self.segundo_numero_entry.get()
        if self.verificar_numeros(num1, num2):
            resultado = (float(num1) * float(num2)) / 100
            self.resultado_entry.config(state="normal")
            self.resultado_entry.delete(0, tk.END)
            self.resultado_entry.insert(0, str(resultado))
            self.resultado_entry.config(state="readonly")
        else:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")

    def reset(self):
        self.primer_numero_entry.delete(0, tk.END)
        self.segundo_numero_entry.delete(0, tk.END)
        self.resultado_entry.config(state="normal")
        self.resultado_entry.delete(0, tk.END)
        self.resultado_entry.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")  
    app = CalculadoraApp(root)
    root.mainloop()
