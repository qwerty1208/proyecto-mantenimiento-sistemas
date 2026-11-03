"""Script autónomo de pruebas para validar la herencia en Backend (OOP y Pydantic) y BD."""

from decimal import Decimal
from backend.esquemas.platillo_esquema import (
    PlatilloBase,
    PlatilloCrear,
    PlatilloRespuesta,
)
from backend.repositorios.repositorio_base import RepositorioBase
from backend.repositorios.repositorio_platillo import RepositorioPlatillo


def probar_herencia_esquemas() -> None:
  print("\n==================================================")
  print(" 1. PRUEBA DE HERENCIA EN ESQUEMAS (PYDANTIC)")
  print("==================================================")

  # Verificar relaciones de subclasificación
  print(
      "✔️ PlatilloCrear hereda de PlatilloBase:"
      f" {issubclass(PlatilloCrear, PlatilloBase)}"
  )
  print(
      "✔️ PlatilloRespuesta hereda de PlatilloBase:"
      f" {issubclass(PlatilloRespuesta, PlatilloBase)}"
  )

  # Instanciación de prueba
  crear = PlatilloCrear(
      nombre_platillo="Tacos al Pastor",
      precio=Decimal("45.00"),
      id_categoria=1,
      calorias=350,
  )
  print(
      f"   [PlatilloCrear] Nombre: '{crear.nombre_platillo}' | Precio:"
      f" ${crear.precio} MXN"
  )

  respuesta = PlatilloRespuesta(
      id_platillo=1,
      nombre_platillo="Tacos al Pastor",
      precio=Decimal("45.00"),
      id_categoria=1,
      calorias=350,
  )
  print(
      f"   [PlatilloRespuesta] ID: {respuesta.id_platillo} | Nombre:"
      f" '{respuesta.nombre_platillo}'"
  )


def probar_herencia_repositorios() -> None:
  print("\n==================================================")
  print(" 2. PRUEBA DE HERENCIA EN REPOSITORIOS (OOP & BD)")
  print("==================================================")

  repo = RepositorioPlatillo()

  # Verificar atributos heredados
  print(
      "✔️ RepositorioPlatillo hereda de RepositorioBase:"
      f" {issubclass(RepositorioPlatillo, RepositorioBase)}"
  )
  print(f"   Tabla configurada en el padre: '{repo.nombre_tabla}'")
  print(f"   Llave primaria en el padre: '{repo.llave_primaria}'")

  # Verificar presencia de métodos
  metodos_padre = ["obtener_todos", "obtener_por_id", "eliminar_por_id"]
  print("\nMétodos heredados de RepositorioBase:")
  for m in metodos_padre:
    print(f"   - {m}(): {'Disponible' if hasattr(repo, m) else 'No disponible'}")

  # Consulta real a Neon PostgreSQL
  print("\nConsultando datos en Neon PostgreSQL...")
  try:
    # Método heredado del padre
    platillos_todos = repo.obtener_todos()
    # Método propio de la clase hija
    platillos_disponibles = repo.obtener_disponibles()

    print(
        " Método heredado 'obtener_todos()' recuperó:"
        f" {len(platillos_todos)} registros."
    )
    print(
        " Método propio 'obtener_disponibles()' recuperó:"
        f" {len(platillos_disponibles)} registros."
    )

    if platillos_disponibles:
      print("\nPlatillos obtenidos desde Neon DB:")
      for p in platillos_disponibles:
        print(
            f"   • ID {p['id_platillo']}: {p['nombre_platillo']} -"
            f" ${p['precio']} MXN"
        )
    else:
      print(" La base de datos no tiene platillos marcados como disponibles.")

  except Exception as error:
    print(f" Error al consultar la base de datos: {error}")


if __name__ == "__main__":
  probar_herencia_esquemas()
  probar_herencia_repositorios()
  print("  PRUEBAS FINALIZADAS EXITOSAMENTE")