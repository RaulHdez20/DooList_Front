from fastapi import APIRouter

router = APIRouter()

@router.get("/Editar")
def editar():
    return [
        {"Accion": "Editar Tarea"},
        {"id": 0, "tarea": "Renombrar Tarea", "hora": "Seleccionar", "status": "Seleccionar"},
    ]
