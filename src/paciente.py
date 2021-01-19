import tkinter as tk

class Paciente:
    """ Clase Paciente que contiene todos los datos de un paciente. """
    def __init__(self):
        self.nombre = tk.StringVar()
        self.dni = tk.IntVar() # el DNI es entero -> es primary key en la BDD
        self.fecha_nac = tk.StringVar()
        self.edad = tk.StringVar()
        self.sexo = tk.StringVar()
        self.telefono = tk.StringVar()
        self.domicilio = tk.StringVar()
        self.barrio = tk.StringVar()
        self.ciudad = tk.StringVar()
      #  self.alergias = tk.StringVar()
      #  self.medicacion = tk.StringVar()
      #  self.enfermedades = tk.StringVar()
      #  self.opt_embarazada = tk.IntVar()
      #  self.opt_fuma = tk.IntVar()
        self.embarazada = False
        self.fuma = False