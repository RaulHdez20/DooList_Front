from fastapi import APIRouter, HTTPException
from app.database.modelos.acciones import Accion

router = APIRouter()

# Simulador de base de datos en memoria
acciones = []

@router.post("/acciones")
def crear_accion(accion: Accion):
    nueva_accion = accion.dict()
    nueva_accion["id"] = len(acciones) + 1
    acciones.append(nueva_accion)
    return {"mensaje": "Acción registrada correctamente", "accion": nueva_accion}

@router.get("/acciones")
def listar_acciones():
    return acciones
