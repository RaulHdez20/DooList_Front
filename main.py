from fastapi import FastAPI
from app.database.database import get_connection

from app.database.rutas.conexion import router as conexion_router
from app.database.rutas.usuarios import router as usuarios_router
from app.database.rutas.tareas import router as tareas_router
from app.database.rutas.eliminar import router as eliminar_router
from app.database.rutas.editar import router as editar_router
from app.database.rutas.completadas import router as completadas_router
from app.database.rutas.fechas import router as fechas_router
from app.database.rutas.verificar import router as verificar_router

app = FastAPI()

# Incluir todos los routers
app.include_router(conexion_router)
app.include_router(usuarios_router)
app.include_router(tareas_router)
app.include_router(eliminar_router)
app.include_router(editar_router)
app.include_router(completadas_router)
app.include_router(fechas_router)
app.include_router(verificar_router)

@app.get("/")
def root():
    return {"mensaje": "Hola, este es el backend sin base de datos"}
