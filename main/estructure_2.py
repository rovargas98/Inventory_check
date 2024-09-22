import pandas as pd
from pathlib import Path
import re

# Definir los colores permitidos (se pueden agregar más)
COLORES_PERMITIDOS = ['negra', 'gris', 'azul', 'verde', 'violeta', 'blanca', 'naranja', 'púrpura', 'transparente', 'rojo', 'negro']

# Función para procesar una línea de texto
def procesar_linea(linea):
    # Expresión regular ajustada para la estructura del archivo
    patron = r'^(.*?)\s+para\s+(Samsung|Apple|Huawei|Xiaomi|Motorola)\s+(.+?)\s+-\s+(\S+)\s+-\s+(.+)$'


    match = re.match(patron, linea)

    if match:
        grupos = match.groups()
        descripcion = grupos[0].strip()  # Descripción del producto
        marca = grupos[1]  # Marca
        modelo = grupos[2].strip()  # Modelo
        color = grupos[3].capitalize() if grupos[3] and grupos[3].lower() in COLORES_PERMITIDOS else ''  # Color
        calidad = grupos[4].strip() if grupos[4] else ''  # Calidad

        return {
            'Descripción': descripcion,
            'Marca': marca,
            'Modelo': modelo,
            'Color': color,
            'Calidad': calidad
        }
    else:
        # Si la línea no coincide con el patrón esperado
        return {
            'Descripción': linea.strip(),
            'Marca': '',
            'Modelo': '',
            'Color': '',
            'Calidad': ''
        }

# Función para convertir un archivo TXT a Excel
def txt_a_excel(ruta_entrada, ruta_salida):
    ruta_archivo = Path(ruta_entrada)

    # Verificar si el archivo existe
    if not ruta_archivo.exists():
        print(f"El archivo {ruta_archivo} no existe.")
        return

    datos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            # Saltar la primera línea si contiene encabezados
            next(file, None)

            for linea in file:
                linea = linea.strip()
                if linea:  # Ignorar líneas vacías
                    datos.append(procesar_linea(linea))

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    if not datos:
        print("No se encontraron datos para procesar.")
        return

    # Crear DataFrame de pandas
    df = pd.DataFrame(datos)

    # Verificar si las columnas clave existen antes de reordenarlas
    columnas_necesarias = ['Descripción', 'Marca', 'Modelo', 'Color', 'Calidad']
    for columna in columnas_necesarias:
        if columna not in df.columns:
            df[columna] = ''

    # Reordenar columnas
    df = df[columnas_necesarias]

    # Guardar el DataFrame como un archivo Excel
    try:
        df.to_excel(ruta_salida, index=False)
        print(f"Archivo Excel generado con éxito: {ruta_salida}")
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")

# Rutas de archivos
ruta_entrada = 'data_modified.txt'
ruta_salida = 'productos_transformados.xlsx'

# Ejecutar la conversión
txt_a_excel(ruta_entrada, ruta_salida)