import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="RaulHdez",
        password="Rulocraft7",
        database="tareas_db"
    )

