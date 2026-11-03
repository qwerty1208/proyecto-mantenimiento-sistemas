"""Módulo de esquemas Pydantic para la entidad Platillo.

Aplica herencia de clases para separar la validación de creación y respuesta.
"""

from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field


class PlatilloBase(BaseModel):
    """Esquema base con los atributos compartidos de un platillo."""

    nombre_platillo: str = Field(
        ..., max_length=120, description="Nombre comercial del platillo"
    )
    descripcion: Optional[str] = Field(
        None, description="Descripción detallada del platillo"
    )
    precio: Decimal = Field(
        ..., ge=0, description="Precio unitario en pesos mexicanos"
    )
    id_categoria: int = Field(
        ..., description="Identificador de la categoría a la que pertenece"
    )
    calorias: int = Field(
        0, ge=0, description="Aporte calórico en kilocalorías"
    )
    ingredientes: Optional[str] = Field(
        None, description="Lista de ingredientes separados por comas"
    )
    alergenos: Optional[str] = Field(
        None, description="Alérgenos conocidos (ej. Gluten, Lácteos)"
    )
    disponible: bool = Field(
        True, description="Estatus de disponibilidad en menú"
    )
    imagen_url: Optional[str] = Field(
        None, description="Ruta o URL de la imagen del platillo"
    )


class PlatilloCrear(PlatilloBase):
    """Esquema para la creación de un nuevo platillo en el sistema."""

    pass


class PlatilloRespuesta(PlatilloBase):
    """Esquema de respuesta devuelto por la API al consultar un platillo."""

    id_platillo: int

    class Config:
        from_attributes = True