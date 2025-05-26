import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="RaulH",
        password="Rulocraft7",
        database="tareas_db",
    )
