"""Módulo para el manejo del pool de conexiones a PostgreSQL."""

from contextlib import contextmanager
from typing import Generator
import psycopg2
from psycopg2.extras import RealDictCursor
from backend.core.config import configuracion
from backend.core.sistema_logs import logger_sistema


@contextmanager
def obtener_conexion() -> Generator[psycopg2.extensions.connection, None, None]:
    conexion = None
    try:
        conexion = psycopg2.connect(
            configuracion.DATABASE_URL,
            sslmode="require",
            cursor_factory=RealDictCursor,
        )
        yield conexion
    except Exception as error:
        logger_sistema.error(f"Error al conectar con PostgreSQL Neon: {error}")
        raise error
    finally:
        if conexion and not conexion.closed:
            conexion.close()