from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

tareas = [
    {"id": 1, "titulo": "Comprar chelas", "descripcion": "Ir a la tienda", "hora": "1:00pm", "status": "No realizada"},
    {"id": 2, "titulo": "Bañar a Tobi", "descripcion": "Usar shampoo antipulgas", "hora": "3:30pm", "status": "Realizada"},
    {"id": 3, "titulo": "Ir al GYM", "descripcion": "Recuerda llevar agua", "hora": "5:00pm", "status": "Pendiente"},
] 

class Tarea(BaseModel):
    titulo: str
    descripcion: str
    hora: str
    status: str

@router.post("/añadirtarea")
def añadir_tarea(tarea: Tarea):
    nueva_tarea = tarea.dict()
    nueva_tarea["id"] = len(tareas) + 1
    tareas.append(nueva_tarea)
    return {"mensaje": "Tarea añadida correctamente", "tarea": nueva_tarea}




@router.get("/todas")
def obtener_todas_las_tareas():
    tareass = [
        {"id": 1, "titulo": "Hacer compras", "descripcion": "Comprar leche y pan", "hora": "10:00am", "status": "Pendiente"},
        {"id": 2, "titulo": "Estudiar", "descripcion": "Repasar FastAPI", "hora": "2:00pm", "status": "Completado"},
        {"id": 3, "titulo": "Ir al gimnasio", "descripcion": "Entrenamiento de pierna", "hora": "6:00pm", "status": "Pendiente"},
    ]
    return tareass
