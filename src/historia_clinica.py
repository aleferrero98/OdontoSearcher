import tkinter as tk
import calendario as cal


#----------------------ficha odontologica---------------------------
class Datos_personales:
    def __init__(self):
        self.raiz = tk.Tk() 
        self.raiz.title("Ficha Odontológica") #Cambiar el nombre de la ventana 
        ancho_ventana = 600
        alto_ventana = 500
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
        img_flecha = tk.PhotoImage(file="../imagenes/flecha.png", width=25, height=25)

        # Variables de control
        self.nombre = tk.StringVar()
        self.dni = tk.StringVar()
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
        self.opt_embarazada = tk.IntVar()
        self.opt_fuma = tk.IntVar()
        self.embarazada = False
        self.fuma = False
        
        #TITULO
        lbl_ficha_odonto = tk.Label(self.frame, text="Ficha Odontológica")
        lbl_ficha_odonto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        lbl_ficha_odonto.config(justify="center")
        
        #Primera parte
        lbl_nombre = tk.Label(self.frame, text="Apellido y nombre:")
        lbl_nombre.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ent_nombre = tk.Entry(self.frame)
        ent_nombre.grid(row=1, column=1, padx=5, pady=5)
        
        lbl_dni = tk.Label(self.frame, text="D.N.I.:")
        lbl_dni.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ent_dni = tk.Entry(self.frame)
        ent_dni.grid(row=2, column=1, padx=5, pady=5)
        
        lbl_fecha_nac = tk.Label(self.frame, text="Fecha de nacimiento:")
        lbl_fecha_nac.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ent_fecha = tk.Entry(self.frame, textvariable=self.fecha_nac)
        ent_fecha.grid(row=3, column=1, padx=5, pady=5)
        btn_flecha = tk.Button(self.frame, image = img_flecha, cursor="hand2", command=lambda:self.abrir_calendario(fecha_nac))
        btn_flecha.grid(row=3, column=2, padx=5, pady=5)

        lbl_edad = tk.Label(self.frame, text="Edad:")
        lbl_edad.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        ent_edad = tk.Entry(self.frame)
        ent_edad.grid(row=4, column=1, padx=5, pady=5)

        lbl_sexo = tk.Label(self.frame, text="Sexo:")
        lbl_sexo.grid(row=4, column=2, sticky="w", padx=5, pady=5)
        ent_sexo = tk.Entry(self.frame)
        ent_sexo.grid(row=4, column=3, padx=5, pady=5)

        lbl_telefono = tk.Label(self.frame, text="Teléfono de contacto:")
        lbl_telefono.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        ent_telefono = tk.Entry(self.frame)
        ent_telefono.grid(row=5, column=1, padx=5, pady=5)

        lbl_domicilio = tk.Label(self.frame, text="Domicilio:")
        lbl_domicilio.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        ent_domicilio = tk.Entry(self.frame)
        ent_domicilio.grid(row=6, column=1, padx=5, pady=5)

        lbl_barrio = tk.Label(self.frame, text="Barrio:")
        lbl_barrio.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        ent_barrio = tk.Entry(self.frame)
        ent_barrio.grid(row=7, column=1, padx=5, pady=5)

        lbl_ciudad = tk.Label(self.frame, text="Ciudad:")
        lbl_ciudad.grid(row=7, column=2, sticky="w", padx=5, pady=5)
        ent_ciudad = tk.Entry(self.frame)
        ent_ciudad.grid(row=7, column=3, padx=5, pady=5)
        
        #segunda parte
        lbl_alergias = tk.Label(self.frame, text="Alergias:")
        lbl_alergias.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        ent_alergias = tk.Entry(self.frame)
        ent_alergias.grid(row=9, column=1, padx=5, pady=5)

        lbl_medicacion = tk.Label(self.frame, text="Medicación actual:")
        lbl_medicacion.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        ent_medicacion = tk.Entry(self.frame)
        ent_medicacion.grid(row=10, column=1, padx=5, pady=5)

        lbl_enfermedades = tk.Label(self.frame, text="Enfermedades sistémicas relevantes:")
        lbl_enfermedades.grid(row=11, column=0, sticky="w", padx=5, pady=5)
        ent_enfermedades = tk.Entry(self.frame)
        ent_enfermedades.grid(row=11, column=1, padx=5, pady=5)
        
        #tercera parte
        lbl_embarazo = tk.Label(self.frame, text="¿Embarazada?")
        lbl_embarazo.grid(row=13, column=0, sticky="w", padx=5, pady=5)
        embarazo_si = tk.Radiobutton(self.frame, text="Si", variable=self.opt_embarazada, value=1, command=self.set_embarazada(True))
        embarazo_si.grid(row=13, column=1, sticky="w", padx=5, pady=5)
        embarazo_no = tk.Radiobutton(self.frame, text="No", variable=self.opt_embarazada, value=2, command=self.set_embarazada(False))
        embarazo_no.grid(row=13, column=2, sticky="w", padx=5, pady=5)

        lbl_fuma = tk.Label(self.frame, text="¿Fuma?")
        lbl_fuma.grid(row=14, column=0, sticky="w", padx=5, pady=5)
        fuma_si = tk.Radiobutton(self.frame, text="Si", variable=self.opt_fuma, value=1, command=self.set_fuma(True))
        fuma_si.grid(row=14, column=1, sticky="w", padx=5, pady=5)
        fuma_no = tk.Radiobutton(self.frame, text="No", variable=self.opt_fuma, value=2, command=self.set_fuma(False))
        fuma_no.grid(row=14, column=2, sticky="w", padx=5, pady=5)

        btn_guardar = tk.Button(self.frame, text="Guardar", cursor="hand2", command=self.guardar_datos)
        btn_guardar.grid(row=15, column=1, padx=5, pady=5)
        btn_cancelar = tk.Button(self.frame, text="Cancelar", cursor="hand2", command=self.cancelar)
        btn_cancelar.grid(row=15, column=2, padx=5, pady=5)

        self.raiz.mainloop()

    def abrir_calendario(self, fecha):
        calendario = cal.Calendario(fecha)

    def set_embarazada(self, valor):
        self.embarazada = valor

    def set_fuma(self, valor):
        self.fuma = valor

    def cancelar(self):
        self.raiz.destroy()

    def guardar_datos(self):
        """guarda los datos en la BDD"""


#---------------------historia clinica-----------------------------
class Historia_clinica:
    def __init__(self):
        self.raiz = tk.Tk() 
        self.raiz.title("Historia clínica") #Cambiar el nombre de la ventana 
        ancho_ventana = 600
        alto_ventana = 500
        x_ventana = self.raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.raiz.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        
        self.raiz.geometry(posicion) #Configurar tamaño 
        self.raiz.iconbitmap('../imagenes/diente.ico') #Cambiar el icono por defecto, debe ser .ico
        self.raiz.config(bg="white") #Cambiar color de fondo
        self.raiz.resizable(False,False)
        
        self.frame = tk.Frame(self.raiz, width=ancho_ventana, height=alto_ventana)
        self.frame.pack() #agrega el Frame al root, el tamaño al que se ajusta es al del frame
        
        # Variables de control
        
        #TITULO
        lbl_hist_clinica = tk.Label(self.frame, text="Historia Clínica")
        lbl_hist_clinica.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        lbl_hist_clinica.config(justify="center")

        #Tabla
        lbl_fecha = tk.Label(self.frame, text="Fecha")
        lbl_fecha.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        lbl_prestacion = tk.Label(self.frame, text="Prestación")
        lbl_prestacion.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        lbl_observaciones = tk.Label(self.frame, text="Observaciones")
        lbl_observaciones.grid(row=1, column=2, sticky="w", padx=5, pady=5)

        self.raiz.mainloop()




ex = Datos_personales()
#ex = Historia_clinica()