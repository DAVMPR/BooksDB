from typing import Optional

ESTADOS_VALIDOS = {"want_to_read", "reading", "readed"}
PROPIEDADES_VALIDAS = {"no_lo_tengo", "fisico", "digital"}

class Book:
    def __init__(self, titulo: str, autor: str, genero_principal: str,
                 genero_secundario: Optional[str] = None,
                 estado: str = "want_to_read", propiedad: str = "no_lo_tengo"):
        self.titulo = titulo
        self.autor = autor
        self.genero_principal = genero_principal
        self.genero_secundario = genero_secundario
        self.estado = estado  # Opciones: "want_to_read", "reading", "readed"
        self.propiedad = propiedad  # Opciones: "no_lo_tengo", "fisico", "digital"

    def __repr__(self):
        return f"<Book '{self.titulo}' by {self.autor}, estado={self.estado}, propiedad={self.propiedad}>"

    def __str__(self):
        return f"📘 '{self.titulo}' de {self.autor} — [{self.estado}] ({self.propiedad})"

    def to_dict(self):
        """Convierte el objeto Book a un diccionario para guardarlo en JSON o CSV"""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero_principal": self.genero_principal,
            "genero_secundario": self.genero_secundario,
            "estado": self.estado,
            "propiedad": self.propiedad
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Crea una instancia Book desde un diccionario (por ejemplo, leído desde JSON)"""
        return cls(
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            genero_principal=data.get("genero_principal"),
            genero_secundario=data.get("genero_secundario"),
            estado=data.get("estado", "want_to_read"),
            propiedad=data.get("propiedad", "no_lo_tengo")
        )