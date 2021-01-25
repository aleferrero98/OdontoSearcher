import tkinter as tk
import base_datos as bdd

class Paciente:
    """ Clase Paciente que contiene todos los datos de un paciente. """
    def __init__(self, id, base_datos):
        self.nombre = tk.StringVar()
        self.dni = tk.IntVar() # el DNI es entero -> es primary key en la BDD
        self.fecha_nac = tk.StringVar()
        self.edad = tk.StringVar()
        self.sexo = tk.StringVar()
        self.telefono = tk.StringVar()
        self.domicilio = tk.StringVar()
        self.barrio = tk.StringVar()
        self.ciudad = tk.StringVar()
        self.alergias = tk.StringVar()
        self.medicacion = tk.StringVar()
        self.enfermedades = tk.StringVar()
        self.opt_embarazada = tk.IntVar() # radiobutton (1-Si, 0-No)
        self.opt_fuma = tk.IntVar() # radiobutton (1-Si, 0-No)
        #self.embarazada = False
        #self.fuma = False
        self.id = id # es el nombre o el dni del paciente
        self.base_datos = base_datos
        self.var_modificadas = {'NOMBRE': '', 'DNI': '',
                                'FECHA_NACIMIENTO': '', 'EDAD': '', 'SEXO': '', 'TELEFONO': '',
                                'DOMICILIO': '', 'BARRIO': '', 'CIUDAD': '',
                                'EMBARAZADA': '', 'FUMA': ''}


    def cargar_datos_paciente(self):
        """ Carga los datos del paciente desde la BDD a las variables de control. 
            Retorna False en caso de que no existan tales datos. """
        datos = self.base_datos.leer_datos("DATOS_PERSONALES", self.id)
        if(datos == []):
            return False
        datos = list(datos[0]) # transforma tupla en lista
        self.nombre.set(datos[0])
        self.dni.set(datos[1])
        self.fecha_nac.set(datos[2])
        self.edad.set(datos[3])
        self.sexo.set(datos[4])
        self.telefono.set(datos[5])
        self.domicilio.set(datos[6])
        self.barrio.set(datos[7])
        self.ciudad.set(datos[8])
        self.alergias.set(datos[9])
        self.medicacion.set(datos[10])
        self.enfermedades.set(datos[11])
        self.opt_embarazada.set(datos[12])
        self.opt_fuma.set(datos[13])
        #self.embarazada = True if(datos[12] == 1) else False
        #self.fuma = True if(datos[13] == 1) else False
        return True

    def detectar_cambio(self):
        """ Detecta si algun StringVar o IntVar cambió de valor para marcarlo como 'modificado'. """
        # my_var.trace_add('write', my_callback) 
        # El valor es el nombre exacto del atributo en la BDD, en lugar de poner True o False.
        #self.nombre.trace('wu', lambda:self.set_variable('NOMBRE', self.nombre.get())) 
        self.nombre.trace_add('write', self.set_nombre) 
        self.dni.trace_add('write', self.set_dni) 
        self.fecha_nac.trace_add('write', self.set_fecha_nac) 
        self.edad.trace_add('write', self.set_edad) 
        self.sexo.trace_add('write', self.set_sexo) 
        self.telefono.trace_add('write', self.set_telefono) 
        self.domicilio.trace_add('write', self.set_domicilio) 
        self.barrio.trace_add('write', self.set_barrio) 
        self.ciudad.trace_add('write', self.set_ciudad) 
        #self.alergias.trace_add('write', self.set_alergias) 
        #self.medicacion.trace_add('write', self.set_medicacion) 
        #self.enfermedades.trace_add('write', self.set_enfermedades) 
        
        self.opt_embarazada.trace_add('write', self.set_opt_embarazada) 
        self.opt_fuma.trace_add('write', self.set_opt_fuma) 

    def set_nombre(self, *args):
        self.var_modificadas['NOMBRE'] = self.nombre.get()
    
    def set_dni(self, *args):
        self.var_modificadas['DNI'] = self.dni.get()

    def set_fecha_nac(self, *args):
        self.var_modificadas['FECHA_NACIMIENTO'] = self.fecha_nac.get()

    def set_edad(self, *args):
        self.var_modificadas['EDAD'] = self.edad.get()

    def set_sexo(self, *args):
        self.var_modificadas['SEXO'] = self.sexo.get()

    def set_telefono(self, *args):
        self.var_modificadas['TELEFONO'] = self.telefono.get()

    def set_domicilio(self, *args):
        self.var_modificadas['DOMICILIO'] = self.domicilio.get()
    
    def set_barrio(self, *args):
        self.var_modificadas['BARRIO'] = self.barrio.get()

    def set_ciudad(self, *args):
        self.var_modificadas['CIUDAD'] = self.ciudad.get()

    def set_opt_embarazada(self, *args):
        self.var_modificadas['EMBARAZADA'] = self.opt_embarazada.get()

    def set_opt_fuma(self, *args):
        self.var_modificadas['FUMA'] = self.opt_fuma.get()

  #  def set_embarazada(self, valor):
  #      self.embarazada = valor

 #   def set_fuma(self, valor):
#        self.fuma = valor

