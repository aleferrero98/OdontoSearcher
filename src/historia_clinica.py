#import calendario
import tkinter as tk


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
        
        # Variables de control
        opt_embarazo = tk.IntVar()
        opt_fuma = tk.IntVar()
        
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
        embarazo_si = tk.Radiobutton(self.frame, text="Si", variable=opt_embarazo, value=1)#, command=imprimir)
        embarazo_si.grid(row=13, column=1, sticky="w", padx=5, pady=5)
        embarazo_no = tk.Radiobutton(self.frame, text="No", variable=opt_embarazo, value=2)#, command=imprimir)
        embarazo_no.grid(row=13, column=2, sticky="w", padx=5, pady=5)

        lbl_fuma = tk.Label(self.frame, text="¿Fuma?")
        lbl_fuma.grid(row=14, column=0, sticky="w", padx=5, pady=5)
        fuma_si = tk.Radiobutton(self.frame, text="Si", variable=opt_fuma, value=1)#, command=imprimir)
        fuma_si.grid(row=14, column=1, sticky="w", padx=5, pady=5)
        fuma_no = tk.Radiobutton(self.frame, text="No", variable=opt_fuma, value=2)#, command=imprimir)
        fuma_no.grid(row=14, column=2, sticky="w", padx=5, pady=5)

        self.raiz.mainloop()

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




#ex = Datos_personales()
ex = Historia_clinica()