# claves primarias (PRIMARY KEY) en SQLite
import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute('''
        CREATE TABLE PRODUCTOS (
            CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
            NOMBRE_ARTICULO VARCHAR(50),
            PRECIO INTEGER,
            SECCION VARCHAR(20)
        )''')

productos = [
    ("AR01", "pelota", 20, "jugueteria"),
    ("AR02", "pantalon", 15, "confeccion"),
    ("AR03", "destornillador", 25, "ferreteria"),
    ("AR04", "jarron", 45, "ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()
miConexion.close()