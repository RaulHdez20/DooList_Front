from pydantic import BaseModel

class Accion(BaseModel):
    titulo: str
    tipo: str
    descripcion: str
    tarea_id: int
