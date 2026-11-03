"""Módulo de capa de servicio para la gestión de Platillos.

Aplica las reglas de negocio, validaciones intermedias y coordina
las operaciones entre los controladores y el repositorio.
"""

from typing import List
from fastapi import HTTPException, status
from backend.repositorios.repositorio_platillo import RepositorioPlatillo
from backend.esquemas.platillo_esquema import PlatilloCrear, PlatilloRespuesta


class PlatilloServicio:
    """Servicio con la lógica de negocio para platillos."""

    def __init__(self) -> None:
        """Inicializa la instancia del repositorio correspondiente."""
        self._repositorio = RepositorioPlatillo()

    def listar_platillos_disponibles(self) -> List[PlatilloRespuesta]:
        """Obtiene la lista de platillos disponibles convertidos a esquemas de respuesta.

        Returns:
            List[PlatilloRespuesta]: Colección de DTOs de platillos.
        """
        registros = self._repositorio.obtener_disponibles()
        return [PlatilloRespuesta(**reg) for reg in registros]

    def obtener_platillo_por_id(self, id_platillo: int) -> PlatilloRespuesta:
        """Recupera un platillo por ID o lanza una excepción de no encontrado.

        Args:
            id_platillo (int): Identificador del platillo.

        Raises:
            HTTPException: 404 si el platillo no existe.

        Returns:
            PlatilloRespuesta: DTO con los detalles del platillo.
        """
        registro = self._repositorio.obtener_por_id(id_platillo)
        if not registro:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Platillo con ID {id_platillo} no fue encontrado.",
            )
        return PlatilloRespuesta(**registro)

    def registrar_platillo(self, datos: PlatilloCrear) -> PlatilloRespuesta:
        """Valida y registra un nuevo platillo en la base de datos.

        Args:
            datos (PlatilloCrear): DTO con los campos del platillo a crear.

        Returns:
            PlatilloRespuesta: DTO del platillo creado.
        """
        registro_creado = self._repositorio.crear_platillo(datos.model_dump())
        return PlatilloRespuesta(**registro_creado)