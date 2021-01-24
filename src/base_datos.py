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
        self.cursor_bdd.execute('''CREATE TABLE IF NOT EXISTS DATOS_PERSONALES 
                                (NOMBRE VARCHAR(50), DNI INTEGER UNIQUE,
                                FECHA_NACIMIENTO VARCHAR(15), EDAD VARCHAR(10), SEXO VARCHAR(20), TELEFONO VARCHAR(20),
                                DOMICILIO VARCHAR(50), BARRIO VARCHAR(30), CIUDAD VARCHAR(20),
                                ALERGIAS TEXT, MEDICACION TEXT, ENFERMEDADES TEXT,
                                EMBARAZADA INTEGER, FUMA INTEGER,
                                PRIMARY KEY (DNI))''')    
#                            ODONTOGRAMA BLOB,
        self.cursor_bdd.execute('''CREATE TABLE IF NOT EXISTS HISTORIA_CLINICA 
                                (FECHA VARCHAR(15), PRESTACION VARCHAR(50), OBSERVACIONES TEXT,
                                DNI INTEGER,
                                FOREIGN KEY (DNI) REFERENCES DATOS_PERSONALES(DNI))''')

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
        print(comando)
        self.cursor_bdd.execute(comando)
        self.conexion_bdd.commit() #confirmamos los cambios a realizar 

    def actualizar_datos(self, tabla, atributo, nuevo_valor, dni):
        """ Actualiza los datos de una entrada en la tabla de la base de datos. """
        comando = "UPDATE " + str(tabla) + " SET " + str(atributo) + "='" + str(nuevo_valor) + "' WHERE DNI='" + str(dni) + "'"
        print(comando)
        self.cursor_bdd.execute(comando)
        self.conexion_bdd.commit()

    def borrar_entrada(self, tabla, clave):
        """ Borra los datos de un usuario """
        if(self.isNumber(str(clave))): # True se paso como parametro el dni
            comando = "DELETE FROM " + str(tabla) + " WHERE DNI='" + str(clave) + "'"
        else: # sino es el nombre del paciente
            comando = "DELETE FROM " + str(tabla) + " WHERE NOMBRE='" + str(clave) + "'"
        
        print(comando)
        self.cursor_bdd.execute(comando)
        self.conexion_bdd.commit()

    def isNumber(self, palabra):
        """ Verifica si el string argumento es un numero (dni) o un string.
            Devuelve True si todo el string es un numero. """
        return any(map(str.isdigit, palabra)) # aplica la funcion isdigit a cada digito del string palabra

    def leer_datos(self, tabla, clave):
        """ Obtiene de la base de datos los datos guardados del usuario especificado
            por su nombre o DNI. 
            Retorna los datos obtenidos. """
        if(self.isNumber(str(clave))): # True se paso como parametro el dni
            comando = "SELECT * FROM " + str(tabla) + " WHERE DNI='" + str(clave) + "'"
        else: # sino es el nombre del paciente
            comando = "SELECT * FROM " + str(tabla) + " WHERE NOMBRE='" + str(clave) + "'"
        
        print(comando)
        self.cursor_bdd.execute(comando)
        datos = self.cursor_bdd.fetchall()
        print(datos)
        return datos

    def create_null(self):
        """ Inserta nuevo registro con todos los campos por defecto. """

    def ejecutar(self, comando):
        """ Ejecuta el comando especificado en el argumento como un string. """
        self.cursor_bdd.execute(str(comando))

if(__name__ == '__main__'):
    bdd = Base_Datos("Base_De_Datos")
    datos = ["Alejandro Ferrero", 40054394, "20/04/1998", "22", "Masculino", "15523673", "Bargellini 527", "Centro", "Suardi, Sta Fe.", "no posee", "ibuprofeno", "covid-19", 2, 2]
    bdd.insertar_datos(datos, "DATOS_PERSONALES")
    ret = bdd.leer_datos("DATOS_PERSONALES", "40054394")
    print(ret)
    #bdd.actualizar_datos("DATOS_PERSONALES", "EDAD", "25", 40054394)
    #bdd.actualizar_datos("DATOS_PERSONALES", "BARRIO", "NVA CBA", 40054394)
    #bdd.borrar_entrada("DATOS_PERSONALES", "Alejandro Ferrero")