import tkinter as tk
from tkinter import ttk
import calendario as cal


#----------------------ficha odontologica---------------------------
class Datos_personales:
    def __init__(self):
        self.raiz = tk.Tk() 
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
      #  self.alergias = tk.StringVar()
      #  self.medicacion = tk.StringVar()
      #  self.enfermedades = tk.StringVar()
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
        ent_nombre = tk.Entry(self.frame, textvariable=self.nombre)
        ent_nombre.grid(row=1, column=1, padx=5, pady=5)
        
        lbl_dni = tk.Label(self.frame, text="DNI:")
        lbl_dni.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ent_dni = tk.Entry(self.frame, textvariable=self.dni)
        ent_dni.grid(row=2, column=1, padx=5, pady=5)
        
        lbl_fecha_nac = tk.Label(self.frame, text="Fecha de nacimiento:")
        lbl_fecha_nac.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ent_fecha = tk.Entry(self.frame, textvariable=self.fecha_nac)
        ent_fecha.grid(row=3, column=1, padx=5, pady=5)
        btn_flecha = tk.Button(self.frame, image = img_flecha, cursor="hand2", command=lambda:self.abrir_calendario(self.fecha_nac))
        btn_flecha.grid(row=3, column=2, padx=5, pady=5)

        lbl_edad = tk.Label(self.frame, text="Edad:")
        lbl_edad.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        ent_edad = tk.Entry(self.frame, textvariable=self.edad)
        ent_edad.grid(row=4, column=1, padx=5, pady=5)

        lbl_sexo = tk.Label(self.frame, text="Sexo:")
        lbl_sexo.grid(row=4, column=2, sticky="w", padx=5, pady=5)
        comb_sexo = ttk.Combobox(self.frame, textvariable=self.sexo)
        comb_sexo.grid(row=4, column=3, padx=5, pady=5)
        comb_sexo["values"] = ["Masculino", "Femenino"]

        lbl_telefono = tk.Label(self.frame, text="Teléfono de contacto:")
        lbl_telefono.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        ent_telefono = tk.Entry(self.frame, textvariable=self.telefono)
        ent_telefono.grid(row=5, column=1, padx=5, pady=5)

        lbl_domicilio = tk.Label(self.frame, text="Domicilio:")
        lbl_domicilio.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        ent_domicilio = tk.Entry(self.frame, textvariable=self.domicilio)
        ent_domicilio.grid(row=6, column=1, padx=5, pady=5)

        lbl_barrio = tk.Label(self.frame, text="Barrio:")
        lbl_barrio.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        ent_barrio = tk.Entry(self.frame, textvariable=self.barrio)
        ent_barrio.grid(row=7, column=1, padx=5, pady=5)

        lbl_ciudad = tk.Label(self.frame, text="Ciudad:")
        lbl_ciudad.grid(row=7, column=2, sticky="w", padx=5, pady=5)
        ent_ciudad = tk.Entry(self.frame, textvariable=self.ciudad)
        ent_ciudad.grid(row=7, column=3, padx=5, pady=5)
        
        #segunda parte
        lbl_alergias = tk.Label(self.frame, text="Alergias:")
        lbl_alergias.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        txt_alergias = tk.Text(self.frame, width=20, height=5)
        txt_alergias.grid(row=9, column=1, padx=5, pady=5)
        scroll_alergias = tk.Scrollbar(self.frame, command=txt_alergias.yview, width=5)
        scroll_alergias.grid(row=9, column=2, sticky="nsew", padx=10, pady=10)
        txt_alergias.config(yscrollcommand=scroll_alergias.set)

        lbl_medicacion = tk.Label(self.frame, text="Medicación actual:")
        lbl_medicacion.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        txt_medicion = tk.Text(self.frame, width=20, height=5)
        txt_medicion.grid(row=10, column=1, padx=5, pady=5)
        scroll_medicion = tk.Scrollbar(self.frame, command=txt_medicion.yview)
        scroll_medicion.grid(row=10, column=2, sticky="nsew", padx=10, pady=10)
        txt_medicion.config(yscrollcommand=scroll_medicion.set)

        lbl_enfermedades = tk.Label(self.frame, text="Enfermedades \nsistémicas relevantes:")
        lbl_enfermedades.grid(row=11, column=0, sticky="w", padx=5, pady=5)
        txt_enfermedades = tk.Text(self.frame, width=20, height=5)
        txt_enfermedades.grid(row=11, column=1, padx=5, pady=5)
        scroll_enfermedades = tk.Scrollbar(self.frame, command=txt_enfermedades.yview)
        scroll_enfermedades.grid(row=11, column=2, sticky="nsew", padx=10, pady=10)
        txt_enfermedades.config(yscrollcommand=scroll_enfermedades.set)
        
        #tercera parte
        lbl_embarazo = tk.Label(self.frame, text="¿Embarazada?")
        lbl_embarazo.grid(row=13, column=0, sticky="w", padx=5, pady=5)
        embarazo_si = tk.Radiobutton(self.frame, text="Si", variable=self.opt_embarazada, value=1, command=lambda:self.set_embarazada(True))
        embarazo_si.grid(row=13, column=1, sticky="w", padx=5, pady=5)
        embarazo_no = tk.Radiobutton(self.frame, text="No", variable=self.opt_embarazada, value=2, command=lambda:self.set_embarazada(False))
        embarazo_no.grid(row=13, column=2, sticky="w", padx=5, pady=5)

        lbl_fuma = tk.Label(self.frame, text="¿Fuma?")
        lbl_fuma.grid(row=14, column=0, sticky="w", padx=5, pady=5)
        fuma_si = tk.Radiobutton(self.frame, text="Si", variable=self.opt_fuma, value=1, command=lambda:self.set_fuma(True))
        fuma_si.grid(row=14, column=1, sticky="w", padx=5, pady=5)
        fuma_no = tk.Radiobutton(self.frame, text="No", variable=self.opt_fuma, value=2, command=lambda:self.set_fuma(False))
        fuma_no.grid(row=14, column=2, sticky="w", padx=5, pady=5)

        btn_guardar = tk.Button(self.frame, text="Guardar", cursor="hand2", command=lambda:self.get_text_input(txt_enfermedades))
        btn_guardar.grid(row=15, column=1, padx=5, pady=5)
        btn_cancelar = tk.Button(self.frame, text="Cancelar", cursor="hand2", command=self.cancelar)
        btn_cancelar.grid(row=15, column=2, padx=5, pady=5)

        self.raiz.mainloop()
        print("NOMBRE:", self.nombre.get())
        print("DNI", self.dni.get())
        print("FECHA NACIMIENTO:", self.fecha_nac.get())
        print("EDAD:", self.edad.get())
        print("SEXO:", self.sexo.get())
        print("TELEFONO:", self.telefono.get())
        print("DOMICILIO:", self.domicilio.get())
        print("BARRIO:", self.barrio.get())
        print("CIUDAD:", self.ciudad.get())
        print("EMBARAZADA:", self.embarazada)
        print("FUMA:", self.fuma)

    def abrir_calendario(self, fecha):
        calendario = cal.Calendario(fecha)

    def set_embarazada(self, valor):
        self.embarazada = valor

    def set_fuma(self, valor):
        self.fuma = valor

    def cancelar(self):
        """ Cierra la ventana """
        self.raiz.destroy()

    def get_text_input(self, texto):
        """ Obtiene el texto almacenado en un cuadro de texto """
        result = texto.get("1.0","end-1c") 
        print(result)
        return result

    def guardar_datos(self):
        """guarda los datos en la BDD"""


#---------------------historia clinica-----------------------------
class Historia_clinica:
    def __init__(self):
        self.raiz = tk.Tk() 
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
        comb_prestacion["values"] = ["EXAMEN CLÍNICO", "CONSULTA DE URGENCIA", 
                                    "CONSULTA PERIÓDICA PREVENTIVA",
                                    "CARIES LIMITADA AL ESMALTE",
                                    "CARIES AMELODENTINARIA CON COMPROMISO PULPAR",
                                    "CARIES PROFUNDA CON COMPROMISO PULPAR",
                                    "TRATAMIENTO ENDODONTICO",
                                    "BIOPULPECTOMIA PARCIAL",
                                    "NECROPULPECTOMIA PARCIAL",
                                    "PROTECCIÓN PULPAR DIRECTA",
                                    "PROTECCIÓN PULPAR INDIRECTA",
                                    "RETRATAMIENTO CONSERVADOR",
                                    "INCRUSTACIÓN",
                                    "CARILLAS",
                                    "PRÓTESIS PARCIAL",
                                    "COMPOSTURA",
                                    "REBASADO",
                                    "DEPURACIÓN",
                                    "TOPICACIÓN CON FLUOR",
                                    "INACTIVACIÓN DE POLICARIESSELLADOR DE FOSAS PUNTOS SURCOS Y FISURAS",
                                    "TRATAMIENTO DE GINGIVITIS",
                                    "TRATAMIENTO DE PERIODONTITIS",
                                    "EXODONCIA"]
        txt_observacion = tk.Text(self.tabla, width=20, height=5)
        txt_observacion.grid(row=num_fila, column=3, padx=5, pady=5)
        scroll_observacion = tk.Scrollbar(self.tabla, command=txt_observacion.yview)
        scroll_observacion.grid(row=num_fila, column=4, sticky="nsew", padx=10, pady=10)
        txt_observacion.config(yscrollcommand=scroll_observacion.set)
        self.indice_fila += 1

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



#ex = Datos_personales()
ex = Historia_clinica()