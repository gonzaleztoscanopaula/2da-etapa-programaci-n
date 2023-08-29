import tkinter as tk

def disminuir_valor():
    valor_actual = int(entrada_valor.get())
    valor_actual -= 1
    entrada_valor.delete(0, tk.END)
    entrada_valor.insert(0, str(valor_actual))

ventana = tk.Tk()
ventana.title("Contador Decreciente")
ventana.geometry("300x150")  
ventana.configure(bg="pink")  

etiqueta_valor_actual = tk.Label(ventana, text="Valor actual:", bg="pink")
etiqueta_valor_actual.place(x=20, y=20)

entrada_valor = tk.Entry(ventana)
entrada_valor.place(x=100, y=20, width=100)

boton_disminuir = tk.Button(ventana, text="-", command=disminuir_valor)
boton_disminuir.place(x=120, y=60, width=60)

ventana.mainloop()
