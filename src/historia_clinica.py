#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import calendario as cal
import paciente as pa
#import base_datos as bdd

#----------------------ficha odontologica---------------------------
class Datos_personales:

    def __init__(self, base_de_datos, id, accion):
        self.base_datos = base_de_datos
        self.id = id
        #self.raiz = tk.Tk() 
        self.raiz = tk.Toplevel() 
        self.raiz.title("Ficha Odontológica") #Cambiar el nombre de la ventana 
        ancho_ventana = 600
        alto_ventana = 650
        x_ventana = self.raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.raiz.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        
        self.raiz.geometry(posicion) #Configurar tamaño 
        self.raiz.iconbitmap('../imagenes/diente.ico') #Cambiar el icono por defecto, debe ser .ico
        self.raiz.config(bg="white") #Cambiar color de fondo
        self.raiz.resizable(False,False)
        
        self.frame = tk.Frame(self.raiz, width=ancho_ventana, height=alto_ventana)
        self.frame.pack() #agrega el Frame al root, el tamaño al que se ajusta es al del frame
        
        #Imagenes
        self.img_flecha = tk.PhotoImage(file="../imagenes/flecha.png", width=25, height=25)

        # Variables de control
        #self.opt_embarazada = tk.IntVar()
        #self.opt_fuma = tk.IntVar()

        # Paciente
        self.paciente = pa.Paciente(self.id, self.base_datos)
        
        #TITULO
        lbl_ficha_odonto = tk.Label(self.frame, text="Ficha Odontológica")
        lbl_ficha_odonto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        lbl_ficha_odonto.config(justify="center")
        
        #Primera parte
        lbl_nombre = tk.Label(self.frame, text="Apellido y nombre:")
        lbl_nombre.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ent_nombre = tk.Entry(self.frame, textvariable=self.paciente.nombre)
        ent_nombre.grid(row=1, column=1, padx=5, pady=5)
        
        lbl_dni = tk.Label(self.frame, text="DNI:")
        lbl_dni.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ent_dni = tk.Entry(self.frame, textvariable=self.paciente.dni)
        ent_dni.grid(row=2, column=1, padx=5, pady=5)
        
        lbl_fecha_nac = tk.Label(self.frame, text="Fecha de nacimiento:")
        lbl_fecha_nac.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ent_fecha = tk.Entry(self.frame, textvariable=self.paciente.fecha_nac)
        ent_fecha.grid(row=3, column=1, padx=5, pady=5)
        self.btn_flecha = tk.Button(self.frame, image=self.img_flecha, cursor="hand2", command=lambda:self.abrir_calendario(self.paciente.fecha_nac))
        #self.btn_flecha = tk.Button(self.frame, cursor="hand2", command=lambda:self.abrir_calendario(paciente.fecha_nac))
        self.btn_flecha.grid(row=3, column=2, padx=5, pady=5)

        lbl_edad = tk.Label(self.frame, text="Edad:")
        lbl_edad.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        ent_edad = tk.Entry(self.frame, textvariable=self.paciente.edad)
        ent_edad.grid(row=4, column=1, padx=5, pady=5)

        lbl_sexo = tk.Label(self.frame, text="Sexo:")
        lbl_sexo.grid(row=4, column=2, sticky="w", padx=5, pady=5)
        comb_sexo = ttk.Combobox(self.frame, textvariable=self.paciente.sexo)
        comb_sexo.grid(row=4, column=3, padx=5, pady=5)
        comb_sexo["values"] = ["Masculino", "Femenino"]

        lbl_telefono = tk.Label(self.frame, text="Teléfono de contacto:")
        lbl_telefono.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        ent_telefono = tk.Entry(self.frame, textvariable=self.paciente.telefono)
        ent_telefono.grid(row=5, column=1, padx=5, pady=5)

        lbl_domicilio = tk.Label(self.frame, text="Domicilio:")
        lbl_domicilio.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        ent_domicilio = tk.Entry(self.frame, textvariable=self.paciente.domicilio)
        ent_domicilio.grid(row=6, column=1, padx=5, pady=5)

        lbl_barrio = tk.Label(self.frame, text="Barrio:")
        lbl_barrio.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        ent_barrio = tk.Entry(self.frame, textvariable=self.paciente.barrio)
        ent_barrio.grid(row=7, column=1, padx=5, pady=5)

        lbl_ciudad = tk.Label(self.frame, text="Ciudad:")
        lbl_ciudad.grid(row=7, column=2, sticky="w", padx=5, pady=5)
        ent_ciudad = tk.Entry(self.frame, textvariable=self.paciente.ciudad)
        ent_ciudad.grid(row=7, column=3, padx=5, pady=5)
        
        #segunda parte
        lbl_alergias = tk.Label(self.frame, text="Alergias:")
        lbl_alergias.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        self.txt_alergias = tk.Text(self.frame, width=20, height=5)
        self.txt_alergias.grid(row=9, column=1, padx=5, pady=5)
        scroll_alergias = tk.Scrollbar(self.frame, command=self.txt_alergias.yview, width=5)
        scroll_alergias.grid(row=9, column=2, sticky="nsew", padx=10, pady=10)
        self.txt_alergias.config(yscrollcommand=scroll_alergias.set)
        

        lbl_medicacion = tk.Label(self.frame, text="Medicación actual:")
        lbl_medicacion.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        self.txt_medicacion = tk.Text(self.frame, width=20, height=5)
        self.txt_medicacion.grid(row=10, column=1, padx=5, pady=5)
        scroll_medicacion = tk.Scrollbar(self.frame, command=self.txt_medicacion.yview)
        scroll_medicacion.grid(row=10, column=2, sticky="nsew", padx=10, pady=10)
        self.txt_medicacion.config(yscrollcommand=scroll_medicacion.set)
        

        lbl_enfermedades = tk.Label(self.frame, text="Enfermedades \nsistémicas relevantes:")
        lbl_enfermedades.grid(row=11, column=0, sticky="w", padx=5, pady=5)
        self.txt_enfermedades = tk.Text(self.frame, width=20, height=5)
        self.txt_enfermedades.grid(row=11, column=1, padx=5, pady=5)
        scroll_enfermedades = tk.Scrollbar(self.frame, command=self.txt_enfermedades.yview)
        scroll_enfermedades.grid(row=11, column=2, sticky="nsew", padx=10, pady=10)
        self.txt_enfermedades.config(yscrollcommand=scroll_enfermedades.set)
        
        
        #tercera parte
        lbl_embarazo = tk.Label(self.frame, text="¿Embarazada?")
        lbl_embarazo.grid(row=13, column=0, sticky="w", padx=5, pady=5)
        embarazo_si = tk.Radiobutton(self.frame, text="Si", variable=self.paciente.opt_embarazada, value=1, command=lambda:self.paciente.set_embarazada(True))
        embarazo_si.grid(row=13, column=1, sticky="w", padx=5, pady=5)
        embarazo_no = tk.Radiobutton(self.frame, text="No", variable=self.paciente.opt_embarazada, value=2, command=lambda:self.paciente.set_embarazada(False))
        embarazo_no.grid(row=13, column=2, sticky="w", padx=5, pady=5)

        lbl_fuma = tk.Label(self.frame, text="¿Fuma?")
        lbl_fuma.grid(row=14, column=0, sticky="w", padx=5, pady=5)
        fuma_si = tk.Radiobutton(self.frame, text="Si", variable=self.paciente.opt_fuma, value=1, command=lambda:self.paciente.set_fuma(True))
        fuma_si.grid(row=14, column=1, sticky="w", padx=5, pady=5)
        fuma_no = tk.Radiobutton(self.frame, text="No", variable=self.paciente.opt_fuma, value=2, command=lambda:self.paciente.set_fuma(False))
        fuma_no.grid(row=14, column=2, sticky="w", padx=5, pady=5)

        btn_guardar = tk.Button(self.frame, text="Guardar", cursor="hand2", command=self.guardar_datos)
        btn_guardar.grid(row=15, column=1, padx=5, pady=5)
        btn_cancelar = tk.Button(self.frame, text="Cancelar", cursor="hand2", command=self.cancelar)
        btn_cancelar.grid(row=15, column=2, padx=5, pady=5)

        #self.play()
        #self.cargar_datos()
        #self.paciente.detectar_cambio()
        #self.raiz.mainloop()
        
      #  print("NOMBRE:", self.paciente.nombre.get())
      #  print("DNI:", self.paciente.dni.get())
      #  print("FECHA NACIMIENTO:", self.paciente.fecha_nac.get())
      #  print("EDAD:", self.paciente.edad.get())
      #  print("SEXO:", self.paciente.sexo.get())
      #  print("TELEFONO:", self.paciente.telefono.get())
      #  print("DOMICILIO:", self.paciente.domicilio.get())
      #  print("BARRIO:", self.paciente.barrio.get())
      #  print("CIUDAD:", self.paciente.ciudad.get())
      #  print("EMBARAZADA:", self.paciente.embarazada)
      #  print("FUMA:", self.paciente.fuma)

    def crear_paciente(self):
        """ Crea una entrada en la base de datos para un nuevo paciente. """
        datos = ['', self.id, '', '', '', '', '', '', '', '', '', '', -1, -1]
        self.base_datos.insertar_datos(datos, "DATOS_PERSONALES")
    
    def play(self):
        self.raiz.mainloop()

    def cargar_datos(self):
        """ Carga los datos desde la BDD a las variables de control. """
        self.paciente.cargar_datos_paciente()
        self.set_text(self.txt_alergias, self.paciente.alergias.get())
        self.set_text(self.txt_medicacion, self.paciente.medicacion.get())
        self.set_text(self.txt_enfermedades, self.paciente.enfermedades.get())
        self.paciente.detectar_cambio()
    
    def abrir_calendario(self, fecha):
        #calendario = cal.Calendario(fecha)
        cal.Calendario(fecha)

    def cancelar(self):
        """ Cierra la ventana """
        self.raiz.destroy()

    def get_text_input(self, text):
        """ Obtiene el texto almacenado en un cuadro de texto """
        result = text.get("1.0","end-1c") 
        #print(result)
        return result

    def set_text(self, text, contenido):
        """ Setea el texto a mostrar en un objeto Text. """
        text.insert("1.0", contenido)

    def guardar_datos(self):
        """guarda los datos en la BDD, ACTUALIZA solo aquellos que fueron modificados."""
        print('GUARDARRRR')
        dict_atributos = self.paciente.var_modificadas
        dni = self.paciente.dni.get()
        for clave in dict_atributos:
            if(dict_atributos[clave] != ''):
                self.base_datos.actualizar_datos("DATOS_PERSONALES", clave, dict_atributos[clave], dni)
        str_alergias = self.get_text_input(self.txt_alergias)
        str_medicacion = self.get_text_input(self.txt_medicacion)
        str_enfermedades = self.get_text_input(self.txt_enfermedades)
        self.base_datos.actualizar_datos("DATOS_PERSONALES", 'ALERGIAS', str_alergias, dni)
        self.base_datos.actualizar_datos("DATOS_PERSONALES", 'MEDICACION', str_medicacion, dni)
        self.base_datos.actualizar_datos("DATOS_PERSONALES", 'ENFERMEDADES', str_enfermedades, dni)
        self.raiz.destroy()


#---------------------historia clinica-----------------------------
class Historia_clinica:
    def __init__(self, base_de_datos):
        self.base_datos = base_de_datos
        self.raiz = tk.Toplevel() 
        self.raiz.title("Historia clínica") #Cambiar el nombre de la ventana 
        self.ancho_ventana = 600
        self.alto_ventana = 500
        x_ventana = self.raiz.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        y_ventana = self.raiz.winfo_screenheight() // 2 - self.alto_ventana // 2
        posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        
        self.raiz.geometry(posicion) #Configurar tamaño 
        self.raiz.iconbitmap('../imagenes/diente.ico') #Cambiar el icono por defecto, debe ser .ico
        self.raiz.config(bg="white") #Cambiar color de fondo
        self.raiz.resizable(False,True)
        
        self.frame = tk.Frame(self.raiz, width=self.ancho_ventana, height=self.alto_ventana)
        self.frame.pack() #agrega el Frame al root, el tamaño al que se ajusta es al del frame
        
        # Imagenes
        self.img_flecha = tk.PhotoImage(file="../imagenes/flecha.png", width=25, height=25)
        
        # Variables de control
        self.fecha = tk.StringVar()
        
        #TITULO
        lbl_hist_clinica = tk.Label(self.frame, text="Historia Clínica")
        lbl_hist_clinica.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        lbl_hist_clinica.config(justify="center")

        #Tabla
        self.tabla = tk.Frame(self.frame, width=self.ancho_ventana, height=20)
        self.tabla.grid(row=2)
        lbl_fecha = tk.Label(self.tabla, text="Fecha")
        lbl_fecha.grid(row=1, column=0, sticky="w", padx=5, pady=5, columnspan=2)
        lbl_prestacion = tk.Label(self.tabla, text="Prestación")
        lbl_prestacion.grid(row=1, column=2, sticky="w", padx=5, pady=5)
        lbl_observaciones = tk.Label(self.tabla, text="Observaciones")
        lbl_observaciones.grid(row=1, column=3, sticky="w", padx=5, pady=5, columnspan=2)

        #1er entrada a tabla
        self.indice_fila = 2
        self.crear_entrada()

        frame_btn = tk.Frame(self.frame, width=self.ancho_ventana, height=20)
        frame_btn.grid(row=3)
        btn_entrada = tk.Button(frame_btn, text="Nueva entrada", cursor="hand2", command=self.crear_entrada)
       # btn_entrada.place(x=50, y=30)
        btn_entrada.grid(row=10, column=1, padx=5, pady=5)
        btn_guardar = tk.Button(frame_btn, text="Guardar", cursor="hand2")#, command=lambda:self.abrir_calendario(self.fecha))
        btn_guardar.grid(row=10, column=2, padx=5, pady=5)
        btn_cancelar = tk.Button(frame_btn, text="Cancelar", cursor="hand2", command=self.cancelar)
        btn_cancelar.grid(row=10, column=3, padx=5, pady=5)

        self.raiz.mainloop()

    def crear_entrada(self):
        """crea una nueva entrada en la tabla"""
        num_fila = self.indice_fila
        ent_fecha = tk.Entry(self.tabla, textvariable=self.fecha)
        ent_fecha.grid(row=num_fila, column=0, padx=5, pady=5)
        btn_flecha = tk.Button(self.tabla, image = self.img_flecha, cursor="hand2", command=lambda:self.abrir_calendario(self.fecha))
        btn_flecha.grid(row=num_fila, column=1, padx=5, pady=5)
        comb_prestacion = ttk.Combobox(self.tabla, width=35, height=20)
        comb_prestacion.grid(row=num_fila, column=2, padx=5, pady=5)
        comb_prestacion["values"] = self.leer_archivo('prestaciones.txt')
        txt_observacion = tk.Text(self.tabla, width=20, height=5)
        txt_observacion.grid(row=num_fila, column=3, padx=5, pady=5)
        scroll_observacion = tk.Scrollbar(self.tabla, command=txt_observacion.yview)
        scroll_observacion.grid(row=num_fila, column=4, sticky="nsew", padx=10, pady=10)
        txt_observacion.config(yscrollcommand=scroll_observacion.set)
        self.indice_fila += 1

    def leer_archivo(self, path):
        """ Funcion que lee un txt linea por linea y devuelve una lista con lo leido. """
        archivo = open(path, 'r', encoding='utf-8')
        contenido = archivo.read()
        #print(contenido)
        lista = contenido.split(sep='\n')
        #print(lista)
        archivo.close()
        return lista

    def abrir_calendario(self, fecha):
        calendario = cal.Calendario(fecha)
    
    def cancelar(self):
        self.raiz.destroy()

    def get_text_input(self, texto):
        result = texto.get("1.0","end-1c")
        print(result)
        return result

    def guardar_datos(self):
        """guarda los datos en la BDD"""



#ex = Datos_personales(6)
#ex = Historia_clinica()