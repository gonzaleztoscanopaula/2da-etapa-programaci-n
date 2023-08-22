import tkinter as tk

def incrementar():
    numero_actual = int(caja1.get())
    numero_actual += 1
    caja1.delete(0, tk.END)
    caja1.insert(0, str(numero_actual))

ventana = tk.Tk()
ventana.title("Contador Creciente")
ventana.geometry("300x150")  # Tamaño más pequeño
ventana.configure(bg="pink")  # Fondo rosa

etiqueta = tk.Label(ventana, text="Valor actual:", bg="pink")
etiqueta.place(x=20, y=20)

caja1 = tk.Entry(ventana)
caja1.place(x=100, y=20, width=100)

boton1 = tk.Button(ventana, text="+", command=incrementar)
boton1.place(x=120, y=60, width=60)

ventana.mainloop()
