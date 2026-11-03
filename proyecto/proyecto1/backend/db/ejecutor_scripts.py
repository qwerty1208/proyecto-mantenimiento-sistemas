"""Módulo ejecutor automatizado de scripts SQL idempotentes."""

from pathlib import Path
import psycopg2
from dotenv import load_dotenv
from backend.core.config import configuracion
from backend.core.sistema_logs import logger_sistema

# Cargar explícitamente las variables de entorno desde el archivo .env
load_dotenv()


class EjecutorScriptsSQL:
  """Administra la lectura y ejecución de archivos SQL en PostgreSQL."""

  def __init__(self, directorio_sql: str = "backend/db/sql") -> None:
    self.url_conexion = configuracion.DATABASE_URL
    self.directorio_sql = Path(directorio_sql)

    if not self.url_conexion:
      logger_sistema.warning(
          "La variable de entorno DATABASE_URL no está configurada."
      )

  def ejecutar_todos_los_scripts(self) -> None:
    """Lee secuencialmente los archivos .sql y los aplica en la base de datos."""
    if not self.directorio_sql.exists():
      logger_sistema.error(
          f"El directorio especificado no existe: {self.directorio_sql}"
      )
      return

    archivos_sql = sorted(self.directorio_sql.glob("*.sql"))

    if not archivos_sql:
      logger_sistema.info(
          f"No se encontraron archivos .sql en {self.directorio_sql}"
      )
      return

    try:
      logger_sistema.info("Conectando a Neon PostgreSQL...")
      conexion = psycopg2.connect(self.url_conexion, sslmode="require")
      cursor = conexion.cursor()

      for archivo in archivos_sql:
        logger_sistema.info(f"Ejecutando script SQL: {archivo.name}")
        with open(archivo, "r", encoding="utf-8") as f:
          contenido_sql = f.read()
          cursor.execute(contenido_sql)

      conexion.commit()
      cursor.close()
      conexion.close()
      logger_sistema.info(
          "Sincronización de la base de datos completada exitosamente."
      )

    except Exception as error:
      logger_sistema.error(
          f"Error durante la ejecución de los scripts SQL: {error}"
      )


if __name__ == "__main__":
  ejecutor = EjecutorScriptsSQL()
  ejecutor.ejecutar_todos_los_scripts()