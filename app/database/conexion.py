from fastapi import APIRouter
from database import get_connection 

router = APIRouter

@router.get("/verificar_conexion")
def verificar_conexion():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"conexion": "exitosa", "resultado": resultado}
    except Exception as e:
        return {"conexion": "fallida", "error": str(e)}

# Este codigo es solo para verificar el estado de conexion de la base de datos 

@router.get("/")
def leer_root():
    return {"mensaje": "Hola, este es el backend sin base de datos"} # Lo que retorna es un mensaje de saludo anunciando que estas en el backend sin base de datos 
