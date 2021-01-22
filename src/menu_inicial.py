#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import sys
from tkinter import messagebox
import base_datos as bdd
import historia_clinica as hc
import calendario as cal

class Menu:
    def __init__(self):
        self.raiz = tk.Tk() 
        self.raiz.title("Odonto Searcher") #Cambiar el nombre de la ventana 
        ancho_ventana = 500
        alto_ventana = 400
        x_ventana = self.raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.raiz.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        
        self.raiz.geometry(posicion) #Configurar tamaño 
        self.raiz.iconbitmap('../imagenes/diente.ico') #Cambiar el icono por defecto, debe ser .ico
        self.raiz.config(bg="white") #Cambiar color de fondo
        self.raiz.resizable(False,False)

        self.frame = tk.Frame(self.raiz, width=500, height=400)
        self.frame.pack() #agrega el Frame al root, el tamaño al que se ajusta es al del frame
        img_fondo = tk.PhotoImage(file="../imagenes/fondo.png")
        canvas_fondo = tk.Canvas(self.frame, width=500, height=400)
        canvas_fondo.place(x=0, y=0)
        #canvas_fondo.pack(side="top")
        canvas_fondo.create_image((0,0), image=img_fondo, anchor="nw")
        #label_paciente = canvas_fondo.create_text(60, 320, text="Paciente", font=("waltograph", 30))

        #canvas_botones = tk.Canvas(self.frame, width=500, height=100)
        #canvas_botones.pack(side="bottom")
        #canvas_botones.place(x=0, y=298)
        #canvas_botones.create_image((0,100), image=img_fondo, anchor="sw")

        # Base de datos
        self.base_datos = bdd.Base_Datos("Base_De_Datos")
       # self.vent_datos_personales = hc.Datos_personales(self.base_datos)
        
        # Variables Control
        self.datos_personales = tk.IntVar()
        self.historia_clinica = tk.IntVar()
        self.odontograma = tk.IntVar()
        self.texto_busqueda = tk.StringVar()

        # Ventanas
        self.vent_hist_clinica = None
        self.vent_datos_personales = None

        # Widgets menu
        # cuadros
        cuadro_nombre = tk.Entry(canvas_fondo, width=20, textvariable=self.texto_busqueda)
        cuadro_nombre.config(fg="black", justify="left", font=("arial", 12))
        #imagenes
        img_lupa = tk.PhotoImage(file="../imagenes/lupa2.png")
        img_borrar = tk.PhotoImage(file="../imagenes/borrar.png", width=50, height=50)
        img_salir = tk.PhotoImage(file="../imagenes/exit.png")
        #img_crear = tk.PhotoImage(file="../imagenes/crear.png", width=50, height=50)
        # botones
        btn_lupa = tk.Button(canvas_fondo, image = img_lupa, cursor="hand2", command=self.buscar_registro)
        #btn_crear = tk.Button(canvas_fondo, image = img_crear, cursor="hand2", width=50, height=50)
        btn_borrar = tk.Button(canvas_fondo, image = img_borrar, cursor="hand2", width=50, height=50, command=self.borrar_registro)
        btn_salir = tk.Button(canvas_fondo, image = img_salir, cursor="hand2", command=self.finalizar_programa)
        #checkbox
        check_datos = tk.Checkbutton(canvas_fondo, text="Datos Personales", variable=self.datos_personales, onvalue=1, offvalue=0)# command=abrir_datos_personales)
        check_hist = tk.Checkbutton(canvas_fondo, text="Historia Clínica", variable=self.historia_clinica, onvalue=1, offvalue=0)# command=abrir_historia_clinica)
        check_odont = tk.Checkbutton(canvas_fondo, text="Odontograma", variable=self.odontograma, onvalue=1, offvalue=0)#, command=abrir_odontograma)

        # Se ubican los widgets en el canvas
        alineacion_Y = 320
        canvas_fondo.create_text(60, alineacion_Y, text="Paciente", font=("waltograph", 30))
        cuadro_window = canvas_fondo.create_window(220, alineacion_Y, window=cuadro_nombre)
        lupa_window = canvas_fondo.create_window(350, alineacion_Y, window=btn_lupa)
        #crear_window = canvas_fondo.create_window(411, alineacion_Y, window=btn_crear)
        borrar_window = canvas_fondo.create_window(470, alineacion_Y, window=btn_borrar)
        salir_window = canvas_fondo.create_window(460, 23, window=btn_salir)
        datos_window = canvas_fondo.create_window(100, 370, window=check_datos)
        hist_clinica_window = canvas_fondo.create_window(240, 370, window=check_hist)
        odonto_window = canvas_fondo.create_window(370, 370, window=check_odont)

        self.raiz.mainloop()   

    def finalizar_programa(self):
        self.base_datos.finalizar_conexion()
        print('Byeee')
        sys.exit(0)
    
    def borrar_registro(self):
        """ Borra el registro indicado por el nombre o dni del paciente
            desde la base de datos. """
        opt_datos = self.datos_personales.get()
        opt_historia = self.historia_clinica.get()
        opt_odonto = self.odontograma.get()

        if(opt_datos == 0 and opt_historia == 0 and opt_odonto == 0):
            messagebox.showwarning("Advertencia", "¡Debe seleccionar la opción a eliminar!")
        if(opt_datos == 1):
            msj = "¿Desea realmente borrar los datos personales de " + str(self.texto_busqueda.get()) + "?"
            ret = messagebox.askokcancel("Borrar registro de paciente", msj)
            print("BORRAR", ret)
            self.base_datos.borrar_entrada("DATOS_PERSONALES", self.texto_busqueda.get())

        if(opt_historia == 1):
            msj = "¿Desea realmente borrar la historia clínica de " + str(self.texto_busqueda.get()) + "?"
            ret = messagebox.askokcancel("Borrar registro de paciente", msj)
            print("BORRAR", ret)
            self.base_datos.borrar_entrada("HISTORIA_CLINICA", self.texto_busqueda.get())

        if(opt_odonto == 1):
            msj = "¿Desea realmente borrar el odontograma de " + str(self.texto_busqueda.get()) + "?"
            ret = messagebox.askokcancel("Borrar registro de paciente", msj)
            print("BORRAR", ret)
            #BORRAR ODONTOGRAMAAAAAAAAAAAAAAA

    def buscar_registro(self):
        """ Carga la historia clinica, datos u odontograma del paciente 
            desde la base de datos, indicado por su dni o nombre. """
        opt_datos = self.datos_personales.get()
        opt_historia = self.historia_clinica.get()
        opt_odonto = self.odontograma.get()

        if(opt_datos == 0 and opt_historia == 0 and opt_odonto == 0):
            messagebox.showwarning("Advertencia", "¡Debe seleccionar la opción a buscar!")
        if(opt_datos == 1):
            print('datos')
            self.vent_datos_personales = hc.Datos_personales(self.base_datos, self.texto_busqueda.get())
            #input("hola:")
        if(opt_historia == 1):
            print('historia')
            self.vent_hist_clinica = hc.Historia_clinica(self.base_datos)
        if(opt_odonto == 1):
            print("ODONTOGRAMA PNG")
        



