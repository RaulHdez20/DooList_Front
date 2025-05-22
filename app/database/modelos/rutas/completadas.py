from fastapi import APIRouter

router = APIRouter()

@router.get("/Completadas")
def completadas():
    return [
        {"Accion": "!FELICIDADES¡TAREA COMPLETADA."},
        {"id": 0, "tarea": "Tarea Completada", "hora": "Finalizado", "status": "Finalizado"},
    ]
