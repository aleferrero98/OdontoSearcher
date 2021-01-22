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
      self.opt_embarazada = tk.IntVar() # radiobutton (1-Si, 2-No)
      self.opt_fuma = tk.IntVar() # radiobutton (1-Si, 2-No)
      self.embarazada = False
      self.fuma = False
      self.id = id # es el nombre o el dni del paciente
      self.base_datos = base_datos
      self.cargar_datos_paciente()

    def cargar_datos_paciente(self):
      datos = self.base_datos.leer_datos("DATOS_PERSONALES", self.id)
      datos = list(datos[0]) # transforma tupla en lista
      print(datos)
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
      self.opt_embarazada = datos[12]
      self.opt_fuma = datos[13]
      self.embarazada = True if(datos[12] == 1) else False
      self.fuma = True if(datos[13] == 1) else False

    def set_embarazada(self, valor):
        self.embarazada = valor

    def set_fuma(self, valor):
        self.fuma = valor