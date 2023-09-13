import tkinter as tk
import mysql.connector

class AlmacenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Almacen")
        self.root.geometry("400x200")

        # Conectar a la base de datos MySQL
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Almacen"
        )

        self.cursor = self.conexion.cursor()

        # Botón para ejecutar la sentencia SELECT
        self.boton_select = tk.Button(root, text="Ejecutar SELECT", command=self.ejecutar_select)
        self.boton_select.pack(pady=20)

        # Etiqueta para mostrar los resultados
        self.resultados_label = tk.Label(root, text="")
        self.resultados_label.pack()

    def ejecutar_select(self):
        query = "SELECT * FROM producto"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        # Mostrar los resultados en la etiqueta
        self.resultados_label.config(text=str(resultados))

if __name__ == "__main__":
    root = tk.Tk()
    app = AlmacenApp(root)
    root.mainloop()
