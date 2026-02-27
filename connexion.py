import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Biblio_Tech"
)

cursor = conn.cursor()
