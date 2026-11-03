"""Punto de entrada principal del servidor FastAPI."""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.controladores import platillo_controlador
from backend.core.sistema_logs import logger_sistema

app = FastAPI(
    title="API Sistema de Gestión de Restaurante", version="1.0.0"
)

# Servir archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
plantillas = Jinja2Templates(directory="templates")

# Registrar controladores
app.include_router(platillo_controlador.router)


@app.on_event("startup")
def evento_inicio() -> None:
  logger_sistema.info("Servidor FastAPI iniciado correctamente.")


@app.get("/", response_class=HTMLResponse, tags=["Vistas"])
def vista_inicio(request: Request) -> HTMLResponse:
  """Servidor de la vista principal del menú."""
  return plantillas.TemplateResponse("index.html", {"request": request})


@app.get("/login", response_class=HTMLResponse, tags=["Vistas"])
def vista_login(request: Request) -> HTMLResponse:
  """Servidor de la vista de inicio de sesión."""
  return plantillas.TemplateResponse("login.html", {"request": request})