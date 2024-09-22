from pathlib import Path
import re


def search_and_modify_text(input_file, search_term, replacements=None, context_size=50):
    input_path = Path(input_file)

    if not input_path.exists():
        print(f"El archivo {input_path} no existe.")
        return

    # Leer el contenido del archivo
    with input_path.open('r', encoding='utf-8') as file:
        content = file.read()

    # Buscar el término y mostrar resultados
    matches = list(re.finditer(re.escape(search_term), content, re.IGNORECASE))
    match_count = len(matches)

    print(f"Se encontraron {match_count} ocurrencias de '{search_term}':")

    for i, match in enumerate(matches, 1):
        start = max(0, match.start() - context_size)
        end = min(len(content), match.end() + context_size)
        context = content[start:end]

        # Resaltar el término encontrado
        highlighted = re.sub(re.escape(search_term),
                             lambda m: f"\033[91m{m.group()}\033[0m",
                             context,
                             flags=re.IGNORECASE)

        print(f"\nCoincidencia {i}:")
        print(f"...{highlighted}...")

    if replacements:
        # Realizar las sustituciones
        for old, new in replacements:
            content = re.sub(re.escape(old), new, content, flags=re.IGNORECASE)

        # Escribir el contenido modificado al archivo
        with input_path.open('w', encoding='utf-8') as file:
            file.write(content)
        print(f"\nSe ha completado la modificación. El resultado se ha guardado en {input_path}")

    return match_count


def get_user_input():
    ruta_archivo = Path('..') / 'data' / 'data.txt'

    search_term = input("¿Qué está buscando? ").strip()

    replace = input("¿Desea realizar algún reemplazo? (s/n): ").strip().lower()
    replacements = []
    if replace == 's':
        while True:
            old = input("Ingrese el texto a reemplazar (o presione Enter para terminar): ").strip()
            if not old:
                break
            new = input(f"Ingrese el texto de reemplazo para '{old}': ").strip()
            replacements.append((old, new))

    return ruta_archivo, search_term, replacements


def main():
    input_file, search_term, replacements = get_user_input()
    search_and_modify_text(input_file, search_term, replacements)


if __name__ == "__main__":
    main()