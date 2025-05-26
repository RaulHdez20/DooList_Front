import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jazmincum14",
        database="tareas_db"
    )
