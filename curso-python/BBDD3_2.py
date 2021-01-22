# claves primarias (PRIMARY KEY) en SQLite
import sqlite3

miConexion = sqlite3.connect("GestionProductos2")
miCursor = miConexion.cursor()

miCursor.execute('''
        CREATE TABLE PRODUCTOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_ARTICULO VARCHAR(50),
            PRECIO INTEGER,
            SECCION VARCHAR(20)
        )''')

productos = [
    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 45, "ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()