# operaciones CRUD -> CREATE, READ, UPDATE y DELETE
import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

#READ
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confeccion'")
#productos = miCursor.fetchall()
#print(productos)

#UPDATE
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#DELETE
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()
miConexion.close()