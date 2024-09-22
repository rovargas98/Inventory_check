from pathlib import Path
import pandas as pd
def procesar_producto(texto_producto):
    if not texto_producto.strip():
        return None
    partes = texto_producto.split("-")
    partes = [parte.strip() for parte in partes]

    if len(partes) < 2:
        return None  # Si no hay suficientes partes, devolver None

    marca_modelo = partes[1].split()
    if len(marca_modelo) == 1:
        marca = ""
        modelo = marca_modelo[0]
    else:
        marca = marca_modelo[0]
        modelo = " ".join(marca_modelo[1:])

    try:
        calidad = partes[-1]
    except IndexError:
        calidad = ""  # Si no hay calidad, dejarla en blanco
    return {
        'Descripción': partes[0],
        'Marca': marca,
        'Modelo': modelo,
        'Color': partes[2] if len(partes) >= 3 else "",
        'Calidad': calidad
    }


def txt_a_excel(archivo_txt, archivo_excel):
    # Leer las líneas del archivo TXT
    with open(archivo_txt, 'r') as archivo:
        lineas = archivo.readlines()
    productos = [procesar_producto(linea.strip()) for linea in lineas]
    productos = [producto for producto in productos if producto is not None]
    df = pd.DataFrame(productos)
    df.to_excel(archivo_excel, index=False)


ruta_archivo_txt = Path('..') / 'data' / 'data_modified.txt'
ruta_archivo_excel = Path('..') / 'data' / 'productos.xlsx'
txt_a_excel(ruta_archivo_txt, ruta_archivo_excel)

print(f"Archivo Excel generado: {ruta_archivo_excel}")
