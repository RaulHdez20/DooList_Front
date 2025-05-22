from fastapi import FastAPI
from database import get_connection

app = FastAPI()

#------------------------- Sacado de Chat ---------------------------------------------------
@app.get("/verificar_conexion")
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

#--------------------------------------------------------------------------------------------
# En este codigo veremos un mensaje principal sin tener que poner un endpoint cuando cargemos el enlace
@app.get("/")
def leer_root():
    return {"mensaje": "Hola, este es el backend sin base de datos"} # Lo que retorna es un mensaje de saludo anunciando que estas en el backend sin base de datos 


# -------------------------------------------------------------------------------------------
# En esta parte del codigo tenemos el Endpoint de Usuarios conectada a la base de datos 
@app.get("/usuarios") # Direccion del Endpoint
def users(): # Aqui comienza la estructuea de nuestra tabla dentro de MySql Workbench
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result# En esta parte nos retorna los usuarios insertados en nuestra base de datos 


# -----------------------------------------------------------------------------------------
# Endpoint Añadir Tarea
@app.get("/añadirtarea") # Este es el enlace de nuestro Endpoint
def tarea():
    tareas = [ # Aqui se crean las tareas 
       {"id": 1, "tarea": "Comprar chelas", "hora":"1:00pm", "status":"No realizada"},# Tenemos la estructura de tareas con: Id, Tarea(Con su nombre), Hora y Status
       {"id": 2, "tarea": "Bañar a Tobi","hora":"3:30pm", "status":"Realizada"},# Tenemos la estructura de tareas con: Id, Tarea(Con su nombre), Hora y Status
       {"id": 3, "tarea": "Ir al GYM","hora":"5:00pm", "status":"Pendiente"},# Tenemos la estructura de tareas con: Id, Tarea(Con su nombre), Hora y Status
    ]
    return tareas # En esta parte nos envia todas las tareas definidas 

# -----------------------------------------------------------------------------------------
# Endpoint Eliminar
@app.get("/Eliminar")  # Este es el enlace del Endpoint de Eliminar
def Elimar():
    EliminarTarea = [
        {"Accion": "Eliminar"},  # Aqui definimos la accionn que hara 
        {"id": 0, "tarea": "Escribir Tarea", "hora":"Seleccionar", "status":"Seleccionar"},  # Y aqui como dejara la estructura de las tareas al dar Eliminar 
    ]                                                                                        
    return EliminarTarea # Aqui nos regresa a la tarea Eliminada pero con los parametros vacios

# -----------------------------------------------------------------------------------------
# Endpoint Editar
@app.get("/Editar")  # Este es el enlace del Endpoint Editar 
def Editar():
    EditarTarea = [
        {"Accion": "Editar Tarea"}, # Esta es nuestra accion que hara 
        {"id": 0, "tarea": "Renombrar Tarea", "hora":"Seleccionar", "status":"Seleccionar"}, # Y aqui tenemos la estructura de la tarea y lo que se puede editar
    ]
    return EditarTarea # Aqui nos regresa la tarea Editada


# -----------------------------------------------------------------------------------------
# Endpoint Completadas
@app.get("/Completadas") # Este es el enlace del Endpoint de Tareas Completadas
def Completadas():
    TareasCompletadas = [
        {"Accion": "!FELICIDADES¡TAREA COMPLETADA."}, # Aqui tenemos un mensaje de que se completo la tarea
        {"id": 0, "tarea": "Tarea Completada", "hora":"Finalizado", "status":"Finalizado"}, # Y aqui como quedaria la estructura de la tarea completada
    ]
    return TareasCompletadas # Nos retorna los parametros de la tarea ya completados 


# -----------------------------------------------------------------------------------------
# Endpoint Con Fecha
@app.get("/tareaconfecha")  # Este es el enlace del Endpoint de la Fecha
def tareaconfecha():
    fechas = [
       {"id": 1, "Mes": "Enero", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"}, # En cada uno definimos un mes con: Id, Mes (con nombre), y los dias que tiene
       {"id": 2, "Mes": "Febrero", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 3, "Mes": "Marzo", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 4, "Mes": "Abril", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 5, "Mes": "Mayo", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 6, "Mes": "Junio", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 7, "Mes": "Julio", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 8, "Mes": "Agosto", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 9, "Mes": "Septiembre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 10, "Mes": "Octubre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 11, "Mes": "Noviembre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 12, "Mes": "Diciembre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
    ]
    return fechas # En esta parte nos devuelve todos los meses que tenemos 
