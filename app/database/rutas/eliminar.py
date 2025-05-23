from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Lista simulada de tareas
tareas = [
    {"id": 1, "titulo": "Comprar chelas", "descripcion": "Ir a la tienda", "hora": "1:00pm", "status": "No realizada"},
    {"id": 2, "titulo": "Bañar a Tobi", "descripcion": "Usar shampoo antipulgas", "hora": "3:30pm", "status": "Realizada"},
    {"id": 3, "titulo": "Ir al GYM", "descripcion": "Recuerda llevar agua", "hora": "5:00pm", "status": "Pendiente"},
]

# Modelo para identificar la tarea a eliminar
class EliminarTarea(BaseModel):
    id: int

# POST y DELETE para eliminar tarea
@router.post("/eliminar")
@router.delete("/eliminar")
def eliminar_tarea(datos: EliminarTarea):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == datos.id:
            tarea_eliminada = tareas.pop(index)
            return {"mensaje": "Tarea eliminada", "tarea": tarea_eliminada}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
