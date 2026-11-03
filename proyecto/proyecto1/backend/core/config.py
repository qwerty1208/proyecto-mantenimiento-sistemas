"""Módulo de configuración global de la aplicación."""

import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Configuracion:
  DATABASE_URL: str = os.getenv(
      "DATABASE_URL",
      "postgresql://neondb_owner:npg_YK0ihlr9HPCw@ep-sparkling-mouse-b45d3jzj-pooler.c-6.us-east-2.aws.neon.tech/neondb?sslmode=require",
  )
  SECRET_KEY: str = os.getenv(
      "SECRET_KEY", "clave_secreta_super_segura_desarrollo_2026"
  )
  ALGORITHM: str = "HS256"


configuracion = Configuracion()