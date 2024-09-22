from pathlib import Path

# Definir la ruta del archivo de entrada
ruta_archivo = Path('..') / 'data' / 'data.txt'

def replace_accented_o(input_file, output_file=None):
    input_path = Path(input_file)

    # Si no se especifica archivo de salida, generar uno con '_modified' en la misma carpeta
    if output_file is None:
        output_path = input_path.with_name(input_path.stem + '_modified' + input_path.suffix)
    else:
        output_path = Path(output_file)

    # Crear la tabla de traducción para los caracteres acentuados
    translation_table = str.maketrans("áéíóú", "aeiou")

    # Leer el contenido del archivo de entrada
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Reemplazar caracteres acentuados usando la tabla de traducción
    modified_content = content.translate(translation_table)

    # Escribir el contenido modificado al archivo de salida
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"Se ha completado el reemplazo. El resultado se ha guardado en {output_path}")

# Llamada a la función
replace_accented_o(ruta_archivo)
