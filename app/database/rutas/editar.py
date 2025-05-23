from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Simulación de tareas
tareas = [
    {"id": 1, "titulo": "Comprar chelas", "descripcion": "Ir a la tienda", "hora": "1:00pm", "status": "No realizada"},
    {"id": 2, "titulo": "Bañar a Tobi", "descripcion": "Usar shampoo antipulgas", "hora": "3:30pm", "status": "Realizada"},
    {"id": 3, "titulo": "Ir al GYM", "descripcion": "Recuerda llevar agua", "hora": "5:00pm", "status": "Pendiente"},
]

# Modelo para editar una tarea
class EditarTarea(BaseModel):
    id: int
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    hora: Optional[str] = None
    status: Optional[str] = None

# POST y PUT para editar tarea
@router.post("/editar")
@router.put("/editar")
def editar_tarea(datos: EditarTarea):
    for tarea in tareas:
        if tarea["id"] == datos.id:
            if datos.titulo is not None:
                tarea["titulo"] = datos.titulo
            if datos.descripcion is not None:
                tarea["descripcion"] = datos.descripcion
            if datos.hora is not None:
                tarea["hora"] = datos.hora
            if datos.status is not None:
                tarea["status"] = datos.status
            return {"mensaje": "Tarea actualizada", "tarea": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
