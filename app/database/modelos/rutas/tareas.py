from fastapi import APIRouter

router = APIRouter()

@router.get("/añadirtarea")
def tarea():
    tareas = [
        {"id": 1, "tarea": "Comprar chelas", "hora": "1:00pm", "status": "No realizada"},
        {"id": 2, "tarea": "Bañar a Tobi", "hora": "3:30pm", "status": "Realizada"},
        {"id": 3, "tarea": "Ir al GYM", "hora": "5:00pm", "status": "Pendiente"},
    ]
    return tareas
