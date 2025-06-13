from library_files.models import Book
from library_files.storage import cargar_libros, guardar_libros
import os

# Funciones auxiliares
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=== 📚 Mi Biblioteca Personal ===")
    print("1. Ver todos los libros")
    print("2. Añadir un libro")
    print("3. Actualizar estado o propiedad de un libro")
    print("4. Ver detalles de un libro")
    print("5. Salir")

def mostrar_libros(libros):
    if not libros:
        print("No hay libros en la base de datos.")
    else:
        for i, libro in enumerate(libros, 1):
            print(f"{i}. {libro}")

def pedir_datos_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero_principal = input("Género principal: ")
    genero_secundario = input("Género secundario (opcional): ") or None
    estado = input("Estado (want_to_read / reading / readed): ")
    propiedad = input("Propiedad (no_lo_tengo / fisico / digital): ")
    descripcion = input("Descripción (opcional): ")
    return Book(titulo, autor, genero_principal, genero_secundario, estado, propiedad, descripcion)

def actualizar_libro(libros):
    mostrar_libros(libros)
    try:
        indice = int(input("Selecciona el número del libro a actualizar: ")) - 1
        if 0 <= indice < len(libros):
            libro = libros[indice]
            print(f"Editando: {libro}")
            nuevo_estado = input(f"Nuevo estado (actual: {libro.estado}) [Enter para mantener]: ") or libro.estado
            nueva_propiedad = input(f"Nueva propiedad (actual: {libro.propiedad}) [Enter para mantener]: ") or libro.propiedad
            editar_descripcion = input(f"Editar o añadir descripción (actual: {libro.descripcion or 'No disponible'}) [Enter para mantener]: ") or libro.descripcion
            libro.descripcion = editar_descripcion
            libro.estado = nuevo_estado
            libro.propiedad = nueva_propiedad
            print("✔ Libro actualizado correctamente.")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("❌ Entrada inválida.")

def ver_detalle_libro(libros: list[Book]):
    mostrar_libros(libros)
    if not libros:
        return

    try:
        indice = int(input("\nSelecciona el número del libro para ver detalles: ")) - 1
        if 0 <= indice < len(libros):
            libro = libros[indice]
            print("\n📖 Información detallada del libro:")
            print(f"📘 Título: {libro.titulo}")
            print(f"✍️  Autor: {libro.autor}")
            print(f"📝 Descripción: {libro.descripcion or 'No disponible'}")
            print(f"🏷️  Género principal: {libro.genero_principal}")
            print(f"🏷️  Género secundario: {libro.genero_secundario or 'Ninguno'}")
            print(f"📚 Estado de lectura: {libro.estado}")
            print(f"📦 Propiedad: {libro.propiedad}")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("❌ Entrada inválida.")

# Programa principal
def main():
    libros = cargar_libros()

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            mostrar_libros(libros)
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            limpiar_pantalla()
            nuevo = pedir_datos_libro()
            libros.append(nuevo)
            guardar_libros(libros)
            print("\n✔ Libro añadido exitosamente.")
            input("Presiona Enter para continuar...")

        elif opcion == "3":
            limpiar_pantalla()
            actualizar_libro(libros)
            guardar_libros(libros)
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            limpiar_pantalla()
            ver_detalle_libro(libros)
            input("\nPresiona Enter para continuar...")

        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()