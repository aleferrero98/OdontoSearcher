import sqlite3

class Base_Datos:
    """ Objeto Base de datos que permite el manejo de la misma,
        es de tipo SQLite. """
    def __init__(self, path):
        self.conexion_bdd = sqlite3.connect(path) #path a la base de datos
        self.cursor_bdd = self.conexion_bdd.cursor()
        self.crear_tablas()

    def finalizar_conexion(self):
        """ Cierra la conexion con la BDD """
        self.conexion_bdd.close()

    def crear_tablas(self):
        """ Crea una tabla con atributos en la Base de datos """
        self.cursor_bdd.execute("CREATE TABLE IF NOT EXISTS DATOS_PERSONALES \
                                (NOMBRE VARCHAR(50), DNI INTEGER,\
                                FECHA_NACIMIENTO VARCHAR(15), EDAD VARCHAR(10), TELEFONO VARCHAR(20),\
                                DOMICILIO VARCHAR(50), BARRIO VARCHAR(30), CIUDAD VARCHAR(20),\
                                ALERGIAS TEXT, MEDICACION TEXT, ENFERMEDADES TEXT,\
                                EMBARAZADA INTEGER, FUMA INTEGER,\
                                PRIMARY KEY (DNI))")    
#                            ODONTOGRAMA BLOB,\
        self.cursor_bdd.execute("CREATE TABLE IF NOT EXISTS HISTORIA_CLINICA \
                                (FECHA VARCHAR(15), PRESTACION VARCHAR(50), OBSERVACIONES TEXT,\
                                DNI INTEGER,\
                                FOREIGN KEY (DNI) REFERENCES DATOS_PERSONALES(DNI))")

    def insertar_datos(self, datos, tabla):
        """ Inserta una nueva entrada (datos del paciente) en la tabla.
            Recibe una lista con todos los datos a insertar """
        valores = ''
        for elem in datos:
            if(type(elem) == str):
                valores += "'" + elem + "'"
            else:
                valores += str(elem)
            valores += ', '
        valores = valores[:len(valores)-2] # elimina la ultima coma y espacio
        comando = 'INSERT INTO ' + tabla + ' VALUES(' + valores + ')'
        self.cursor_bdd.execute(comando)
        self.conexion_bdd.commit() #confirmamos los cambios a realizar 

    def actualizar_datos(self):
        """ Actualiza los datos de una entrada en la tabla de la base de datos """

    def borrar_entrada(self):
        """ Borra los datos de un usuario """

bdd = Base_Datos("C:/Users/alejandro/Desktop/Base_de_Datos")