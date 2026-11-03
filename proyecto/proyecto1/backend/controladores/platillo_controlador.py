"""Módulo de endpoints REST para la gestión de platillos.

Define las rutas HTTP para listar, obtener y registrar platillos.
"""

from typing import List
from fastapi import APIRouter, status
from backend.esquemas.platillo_esquema import PlatilloCrear, PlatilloRespuesta
from backend.servicios.platillo_servicio import PlatilloServicio

router = APIRouter(prefix="/api/platillos", tags=["Platillos"])
_servicio = PlatilloServicio()


@router.get(
    "/",
    response_model=List[PlatilloRespuesta],
    status_code=status.HTTP_200_OK,
)
def listar_platillos() -> List[PlatilloRespuesta]:
    """Obtiene el catálogo de platillos actualmente disponibles."""
    return _servicio.listar_platillos_disponibles()


@router.get(
    "/{id_platillo}",
    response_model=PlatilloRespuesta,
    status_code=status.HTTP_200_OK,
)
def obtener_platillo(id_platillo: int) -> PlatilloRespuesta:
    """Obtiene la información detallada de un platillo específico por su ID."""
    return _servicio.obtener_platillo_por_id(id_platillo)


@router.post(
    "/",
    response_model=PlatilloRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_platillo(datos: PlatilloCrear) -> PlatilloRespuesta:
    """Registra un nuevo platillo en el sistema."""
    return _servicio.registrar_platillo(datos)