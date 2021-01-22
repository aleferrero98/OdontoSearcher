# clausula UNIQUE 

import sqlite3

miConexion = sqlite3.connect("GestionProductos2")
miCursor = miConexion.cursor()

miCursor.execute('''
        CREATE TABLE if not exists PRODUCTOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
            PRECIO INTEGER,
            SECCION VARCHAR(20)
        )''')

productos = [
    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 45, "ceramica"),
    ("PANTALON", 11, "confeccion"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()