"""Módulo repositorio base genérico.

Aplica el patrón de herencia para proveer operaciones CRUD estandarizadas
a todas las entidades del sistema.
"""

from typing import Any, Dict, List, Optional
from backend.db.conexion import obtener_conexion
from backend.core.sistema_logs import logger_sistema


class RepositorioBase:
    """Clase padre que abstrae las operaciones básicas de acceso a datos.

    Atributos:
        nombre_tabla (str): Nombre de la tabla en la base de datos PostgreSQL.
        llave_primaria (str): Nombre del campo identificador principal.
    """

    def __init__(self, nombre_tabla: str, llave_primaria: str) -> None:
        """Inicializa la entidad objetivo para las consultas genéricas.

        Args:
            nombre_tabla (str): Tabla de PostgreSQL sobre la que operará.
            llave_primaria (str): Campo de clave primaria (ej. 'id_platillo').
        """
        self.nombre_tabla = nombre_tabla
        self.llave_primaria = llave_primaria

    def obtener_todos(self) -> List[Dict[str, Any]]:
        """Recupera todos los registros activos de la tabla.

        Returns:
            List[Dict[str, Any]]: Lista de registros formateados como diccionarios.
        """
        sql = f"SELECT * FROM {self.nombre_tabla};"
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def obtener_por_id(self, id_registro: int) -> Optional[Dict[str, Any]]:
        """Busca un registro específico por su clave primaria.

        Args:
            id_registro (int): Identificador único del registro.

        Returns:
            Optional[Dict[str, Any]]: Registro encontrado o None si no existe.
        """
        sql = f"SELECT * FROM {self.nombre_tabla} WHERE {self.llave_primaria} = %s;"
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql, (id_registro,))
                return cursor.fetchone()

    def eliminar_por_id(self, id_registro: int) -> bool:
        """Elimina físicamente un registro por su clave primaria.

        Args:
            id_registro (int): Identificador único del registro a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario.
        """
        sql = f"DELETE FROM {self.nombre_tabla} WHERE {self.llave_primaria} = %s;"
        try:
            with obtener_conexion() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(sql, (id_registro,))
                    conexion.commit()
                    return cursor.rowcount > 0
        except Exception as error:
            logger_sistema.error(
                f"Error al eliminar en {self.nombre_tabla}: {error}"
            )
            return False