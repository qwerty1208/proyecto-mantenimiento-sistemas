"""Módulo de auditoría y gestión de logs locales para el sistema de restaurantes.

Este módulo provee una instancia configurada de logging para registrar
eventos del servidor, errores y modificaciones de datos en la bitácora local.
"""

import logging
import sys
from pathlib import Path


class GestorLogs:
    """Administra la configuración del sistema de bitácora local de la aplicación.

    Atributos:
        nombre_logger (str): Nombre identificador del logger principal.
        archivo_log (str): Nombre del archivo donde se almacenará la bitácora.
    """

    def __init__(
        self,
        nombre_logger: str = "restaurante_app",
        archivo_log: str = "bitacora_sistema.log",
    ) -> None:
        """Inicializa los manejadores de salida para la consola y el archivo local.

        Args:
            nombre_logger (str): Nombre único para la instancia de logging.
            archivo_log (str): Nombre del archivo de salida dentro de la
              carpeta logs.
        """
        self._logger = logging.getLogger(nombre_logger)
        self._logger.setLevel(logging.INFO)

        if not self._logger.handlers:
            formato = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

            # Manejador para salida en consola
            manejador_consola = logging.StreamHandler(sys.stdout)
            manejador_consola.setFormatter(formato)
            self._logger.addHandler(manejador_consola)

            # Manejador para archivo local
            directorio_logs = Path("logs")
            directorio_logs.mkdir(parents=True, exist_ok=True)

            manejador_archivo = logging.FileHandler(
                directorio_logs / archivo_log, encoding="utf-8"
            )
            manejador_archivo.setFormatter(formato)
            self._logger.addHandler(manejador_archivo)

    def obtener_logger(self) -> logging.Logger:
        """Retorna la instancia configurada del objeto Logger.

        Returns:
            logging.Logger: Instancia lista para registrar eventos.
        """
        return self._logger


# Instancia global exportable para el uso de todo el backend
logger_sistema = GestorLogs().obtener_logger()