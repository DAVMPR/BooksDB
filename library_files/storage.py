import json
from typing import List
from library_files.models import Book  # Modificada esta línea

ARCHIVO_JSON = "libros.json"

def guardar_libros(libros: List[Book], archivo: str = ARCHIVO_JSON):
    """Guarda una lista de libros en formato JSON"""
    with open(archivo, "w", encoding="utf-8") as f:
        data = [libro.to_dict() for libro in libros]
        json.dump(data, f, ensure_ascii=False, indent=4)

def cargar_libros(archivo: str = ARCHIVO_JSON) -> List[Book]:
    """Carga libros desde un archivo JSON. Devuelve una lista de objetos Book"""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]
    except FileNotFoundError:
        return []  # Si no existe el archivo aún, devuelve lista vacía