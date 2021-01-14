#conectar con BDD SQLite, crear tablas e insertar datos
#VISOR DE BDD SQLITE -> DB Browser for SQLite
import sqlite3

miConexion = sqlite3.connect("BaseDeDatos")
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('raqueta', 10, 'asdfghjkiuytrewDEPORTES')")
miConexion.commit() #confirmamos los cambios a realizar en la tabla

miConexion.close()