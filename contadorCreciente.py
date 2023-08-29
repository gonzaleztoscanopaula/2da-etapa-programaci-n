import tkinter as tk

def incrementar_contador():
    valor_actual = int(entrada_contador.get())
    valor_actual += 1
    entrada_contador.delete(0, tk.END)
    entrada_contador.insert(0, str(valor_actual))

ventana = tk.Tk()
ventana.title("Contador Creciente")
ventana.geometry("300x150")  
ventana.configure(bg="pink")  

etiqueta_valor_actual = tk.Label(ventana, text="Valor actual:", bg="pink")
etiqueta_valor_actual.place(x=20, y=20)

entrada_contador = tk.Entry(ventana)
entrada_contador.place(x=100, y=20, width=100)
entrada_contador.insert(0, "0")  # Inicializar el valor en 0

boton_incrementar = tk.Button(ventana, text="+", command=incrementar_contador)
boton_incrementar.place(x=120, y=60, width=60)

ventana.mainloop()
