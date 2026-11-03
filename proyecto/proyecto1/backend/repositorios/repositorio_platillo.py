"""Módulo de repositorio específico para Platillos.

Hereda de RepositorioBase y añade métodos de consulta especializados.
"""

from typing import Any, Dict, List
from backend.repositorios.repositorio_base import RepositorioBase
from backend.db.conexion import obtener_conexion


class RepositorioPlatillo(RepositorioBase):
    """Gestor de consultas SQL específicas para la tabla platillos."""

    def __init__(self) -> None:
        """Inicializa el repositorio base configurando la tabla 'platillos'."""
        super().__init__(nombre_tabla="platillos", llave_primaria="id_platillo")

    def obtener_disponibles(self) -> List[Dict[str, Any]]:
        """Recupera únicamente los platillos que estén marcados como disponibles.

        Returns:
            List[Dict[str, Any]]: Lista de platillos disponibles.
        """
        sql = "SELECT * FROM platillos WHERE disponible = TRUE;"
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def crear_platillo(self, datos_platillo: Dict[str, Any]) -> Dict[str, Any]:
        """Inserta un nuevo platillo en la base de datos y retorna el objeto creado.

        Args:
            datos_platillo (Dict[str, Any]): Diccionario con los datos del platillo.

        Returns:
            Dict[str, Any]: Registro recién insertado incluyendo su id_platillo.
        """
        sql = """
            INSERT INTO platillos (
                nombre_platillo, descripcion, precio, id_categoria,
                calorias, ingredientes, alergenos, disponible, imagen_url
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *;
        """
        valores = (
            datos_platillo["nombre_platillo"],
            datos_platillo.get("descripcion"),
            datos_platillo["precio"],
            datos_platillo["id_categoria"],
            datos_platillo.get("calorias", 0),
            datos_platillo.get("ingredientes"),
            datos_platillo.get("alergenos"),
            datos_platillo.get("disponible", True),
            datos_platillo.get("imagen_url"),
        )
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql, valores)
                conexion.commit()
                return cursor.fetchone()