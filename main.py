from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI"}

@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., title="ID del ítem", description="El ID único del ítem", ge=1),
    q: str = Query(None, min_length=3, max_length=50, description="Filtro de búsqueda opcional"),
    limit: int = Query(10, description="Cantidad máxima de resultados", ge=1, le=100)
):
    """
    Obtiene un ítem por su ID, con filtros opcionales.
    item_id: el identificador único del ítem.,
    q: filtro de búsqueda opcional por texto.,
    limit: cantidad máxima de resultados a devolver (por defecto 10)."""
    return {"item_id": item_id, "q": q, "limit": limit}