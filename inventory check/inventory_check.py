import customtkinter as ctk
import pandas as pd
from tkinter import messagebox, Listbox
import os

# Nombre del archivo de Excel
file_name = "inventario_pandas.xlsx"

# Crear archivo Excel si no existe
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Descripción", "Marca", "Modelo", "Color", "Calidad"])
    df.to_excel(file_name, index=False)


# Funciones del programa
def cargar_datos():
    """Carga los datos del archivo de Excel al Listbox."""
    exc = pd.read_excel(file_name)
    listbox.delete(0, ctk.END)
    for index, row in exc.iterrows():
        listbox.insert(ctk.END, str(row))


def agregar_producto():
    """Agrega un nuevo producto al archivo Excel."""
    descripcion = entry_descripcion.get()
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    color = entry_color.get()
    calidad = entry_calidad.get()

    if descripcion and marca and modelo and color and calidad:
        nuevo_producto = pd.DataFrame([[descripcion, marca, modelo, color, calidad]],
                                      columns=["Descripción", "Marca", "Modelo", "Color", "Calidad"])
        conch = pd.read_excel(file_name)
        conch = pd.concat([conch, nuevo_producto], ignore_index=True)
        conch.to_excel(file_name, index=False)
        cargar_datos()
        limpiar_campos()
        messagebox.showinfo("Información", "Producto agregado con éxito")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")


def buscar_producto():
    """Busca un producto en el archivo Excel y lo muestra en la lista."""
    buscar = entry_buscar.get()
    excel = pd.read_excel(file_name)
    productos = excel[excel.apply(lambda wow: buscar.lower() in wow.astype(str).str.lower().values, axis=1)]

    listbox.delete(0, ctk.END)
    if not productos.empty:
        for index, row in productos.iterrows():
            listbox.insert(ctk.END, str(row))
    else:
        messagebox.showinfo("Información", "No se encontró el producto")


def modificar_producto():
    """Modifica el producto seleccionado en el Listbox."""
    selection = listbox.curselection()
    if selection:
        excel = pd.read_excel(file_name)
        fila = selection[0]  # Índice de la fila seleccionada

        # Modificar los valores de la fila seleccionada
        excel.loc[fila, "Descripción"] = entry_descripcion.get()
        excel.loc[fila, "Marca"] = entry_marca.get()
        excel.loc[fila, "Modelo"] = entry_modelo.get()
        excel.loc[fila, "Color"] = entry_color.get()
        excel.loc[fila, "Calidad"] = entry_calidad.get()

        excel.to_excel(file_name, index=False)
        cargar_datos()
        limpiar_campos()
        messagebox.showinfo("Información", "Producto modificado con éxito")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un producto para modificar")


def eliminar_producto():
    """Elimina el producto seleccionado del archivo Excel."""
    selection = listbox.curselection()
    if selection:
        excel = pd.read_excel(file_name)
        fila = selection[0]  # Índice de la fila seleccionada
        excel = excel.drop(fila).reset_index(drop=True)
        excel.to_excel(file_name, index=False)
        cargar_datos()
        limpiar_campos()
        messagebox.showinfo("Información", "Producto eliminado con éxito")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar")


def limpiar_campos():
    """Limpia los campos de entrada."""
    entry_descripcion.delete(0, ctk.END)
    entry_marca.delete(0, ctk.END)
    entry_modelo.delete(0, ctk.END)
    entry_color.delete(0, ctk.END)
    entry_calidad.delete(0, ctk.END)
    entry_buscar.delete(0, ctk.END)


# Configuración de la ventana principal
app = ctk.CTk()
app.title("Gestión de Inventario con pandas")
app.geometry("600x400")

# Campos de entrada
label_descripcion = ctk.CTkLabel(app, text="Descripción:")
label_descripcion.grid(row=0, column=0, padx=10, pady=5)
entry_descripcion = ctk.CTkEntry(app)
entry_descripcion.grid(row=0, column=1, padx=10, pady=5)

label_marca = ctk.CTkLabel(app, text="Marca:")
label_marca.grid(row=1, column=0, padx=10, pady=5)
entry_marca = ctk.CTkEntry(app)
entry_marca.grid(row=1, column=1, padx=10, pady=5)

label_modelo = ctk.CTkLabel(app, text="Modelo:")
label_modelo.grid(row=2, column=0, padx=10, pady=5)
entry_modelo = ctk.CTkEntry(app)
entry_modelo.grid(row=2, column=1, padx=10, pady=5)

label_color = ctk.CTkLabel(app, text="Color:")
label_color.grid(row=3, column=0, padx=10, pady=5)
entry_color = ctk.CTkEntry(app)
entry_color.grid(row=3, column=1, padx=10, pady=5)

label_calidad = ctk.CTkLabel(app, text="Calidad:")
label_calidad.grid(row=4, column=0, padx=10, pady=5)
entry_calidad = ctk.CTkEntry(app)
entry_calidad.grid(row=4, column=1, padx=10, pady=5)

# Botones de acciones
btn_agregar = ctk.CTkButton(app, text="Agregar", command=agregar_producto)
btn_agregar.grid(row=5, column=0, padx=10, pady=10)

btn_modificar = ctk.CTkButton(app, text="Modificar", command=modificar_producto)
btn_modificar.grid(row=5, column=1, padx=10, pady=10)

btn_eliminar = ctk.CTkButton(app, text="Eliminar", command=eliminar_producto)
btn_eliminar.grid(row=5, column=2, padx=10, pady=10)

# Campo y botón de búsqueda
label_buscar = ctk.CTkLabel(app, text="Buscar:")
label_buscar.grid(row=6, column=0, padx=10, pady=5)
entry_buscar = ctk.CTkEntry(app)
entry_buscar.grid(row=6, column=1, padx=10, pady=5)

btn_buscar = ctk.CTkButton(app, text="Buscar", command=buscar_producto)
btn_buscar.grid(row=6, column=2, padx=10, pady=5)

# Lista para mostrar los datos del inventario (usando Listbox estándar de tkinter)
listbox = Listbox(app, width=50, height=10)
listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Cargar los datos al iniciar
cargar_datos()

# Iniciar la aplicación
app.mainloop()
