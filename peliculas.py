import tkinter as tk

def agregar_pelicula():
    pelicula = caja_insertar.get()
    if pelicula:
        lista_peliculas.insert(tk.END, pelicula)
        caja_insertar.delete(0, tk.END)

def eliminar_ultima_pelicula():
    if lista_peliculas.size() > 0:
        lista_peliculas.delete(tk.END)

ventana = tk.Tk()
ventana.title("Películas")
ventana.configure(bg="pink")  # Fondo rosa
ventana.geometry("400x400")  # Tamaño de la ventana

etiqueta_ingresar = tk.Label(ventana, text="Ingresa el título de una película:", bg="pink")
etiqueta_ingresar.place(x=20, y=20)

etiqueta_lista_peliculas = tk.Label(ventana, text="Películas:", bg="pink")
etiqueta_lista_peliculas.place(x=260, y=20)

caja_insertar = tk.Entry(ventana)
caja_insertar.place(x=20, y=60, width=180)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_pelicula)
boton_agregar.place(x=20, y=100, width=180)

lista_peliculas = tk.Listbox(ventana)
lista_peliculas.place(x=260, y=60, width=120, height=200)

boton_eliminar = tk.Button(ventana, text="Eliminar última", command=eliminar_ultima_pelicula)
boton_eliminar.place(x=260, y=270, width=120)

# Iniciar el ciclo principal de la GUI
ventana.mainloop()
