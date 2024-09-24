import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Creo la ventana
window = tk.Tk()
window.title("Piezas de Power")

# Genera un margen interior en el programa
frame = tk.Frame(window)
frame.pack()

# Guardando la información de usuario
user_info_frame = tk.LabelFrame(frame, text="Nueva parte")
user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)

# Creando los widgets dentro del grid
modelo_label = tk.Label(user_info_frame, text="Modelo")
model_entry = tk.Entry(user_info_frame)
modelo_label.grid(row=0, column=0)
model_entry.grid(row=1, column=0)

marca_label = tk.Label(user_info_frame, text="Marca")
title_combobox = ttk.Combobox(user_info_frame, values=["iphone", "samsung", "xiaomi", "oppo"])
marca_label.grid(row=0, column=1)
title_combobox.grid(row=1, column=1)

descripcion_label = tk.Label(user_info_frame, text="Descripción")
descripcion_entry = tk.Entry(user_info_frame)
descripcion_label.grid(row=0, column=2)
descripcion_entry.grid(row=1, column=2)

color_label = tk.Label(user_info_frame, text="Color")
color_entry = ttk.Combobox(user_info_frame, values=["verde", "azul", "naranja", "amarillo", "rojo"])
color_label.grid(row=0, column=3)
color_entry.grid(row=1, column=3)

cantidad_label = tk.Label(user_info_frame, text="Cantidad")
cantidad_spinbox = tk.Spinbox(user_info_frame, from_=1, to=110)
cantidad_label.grid(row=0, column=4)
cantidad_spinbox.grid(row=1, column=4)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=15, pady=5)

# Interfaz para buscar
busqueda_frame = tk.LabelFrame(frame, text="Buscar Parte")
busqueda_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

# Cuadro de búsqueda
busqueda_label = tk.Label(busqueda_frame, text="Buscar Parte:")
busqueda_entry = tk.Entry(busqueda_frame, width=110)
busqueda_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
busqueda_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Opción de borrar
borrar_check = tk.Checkbutton(busqueda_frame, text="Borrar artículo")
borrar_check.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Cuadro de resultados
resultado_label = tk.Label(busqueda_frame, text="Resultados:")
resultado_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
resultado_entry = tk.Text(busqueda_frame, height=10, width=90)  # Hacemos el cuadro de resultados más grande
resultado_entry.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Expandir el cuadro de resultados para que ocupe más espacio en la interfaz
busqueda_frame.grid_columnconfigure(0, weight=1)
busqueda_frame.grid_rowconfigure(2, weight=1)

# Ajustar el padding para todos los widgets dentro del busqueda_frame
for widget in busqueda_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Función para exportar datos a Excel usando pandas
def export_to_excel():
    modelo = model_entry.get()
    marca = title_combobox.get()
    descripcion = descripcion_entry.get()
    cantidad = cantidad_spinbox.get()

    # Crear un DataFrame con los datos capturados
    new_data = pd.DataFrame({
        "Modelo": [modelo],
        "Marca": [marca],
        "Descripción": [descripcion],
        "Cantidad": [cantidad]
    })

    file_path = "piezas_power_pandas.xlsx"

    # Si el archivo ya existe, leerlo y añadir los nuevos datos
    if os.path.exists(file_path):
        existing_data = pd.read_excel(file_path)
        new_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Exportar los datos al archivo Excel
    new_data.to_excel(file_path, index=False)

    # Notificación al usuario
    print("Datos exportados a Excel correctamente.")


# Crear un botón para exportar los datos
export_button = tk.Button(frame, text="Exportar a Excel", command=export_to_excel)
export_button.grid(row=2, column=0, sticky="news", padx=20, pady=20)  # Asigna una nueva fila para el botón

# Ejecutar la ventana
window.mainloop()
