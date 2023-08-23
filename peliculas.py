import tkinter as tk

def agregar_pelicula():
    pelicula = caja1_insertar.get()
    if pelicula:
        listbox_peliculas.insert(tk.END, pelicula)
        caja1_insertar.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Películas")
ventana.configure(bg="pink")  # Fondo rosa
ventana.geometry("400x300")  # Tamaño de la ventana

etiqueta_escribir = tk.Label(ventana, text="Escribe el título de una película:", bg="pink")
etiqueta_escribir.place(x=20, y=20)

etiqueta_peliculas = tk.Label(ventana, text="Películas:", bg="pink")
etiqueta_peliculas.place(x=260, y=20)

caja_insertar = tk.Entry(ventana)
caja_insertar.place(x=20, y=60, width=180)

boton_añadir = tk.Button(ventana, text="Añadir", command=agregar_pelicula)
boton_añadir.place(x=20, y=100, width=180)

listbox_peliculas = tk.Listbox(ventana)
listbox_peliculas.place(x=260, y=60, width=120, height=200)

# Iniciar el ciclo principal de la GUI
ventana.mainloop()
