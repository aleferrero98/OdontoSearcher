#import calendario
import tkinter as tk


#----------------------ficha odontologica---------------------------
class Datos_personales:
    def __init__(self):
        self.raiz = tk.Tk() 
        self.raiz.title("Ficha Odontológica") #Cambiar el nombre de la ventana 
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

        lbl_ficha_odonto = tk.Label(self.frame, text="Ficha Odontológica")
        lbl_ficha_odonto.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        lbl_nombre = tk.Label(self.frame, text="Apellido y nombre:")
        lbl_nombre.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        lbl_dni = tk.Label(self.frame, text="D.N.I.:")
        lbl_dni.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        
        
        self.raiz.mainloop()

#---------------------historia clinica-----------------------------
"""

lbl_fecha_nac
lbl_edad
lbl_sexo
lbl_telefono
lbl_domicilio
lbl_barrio
lbl_ciudad

lbl_alergias
lbl_medicacion
lbl_enfermedades

lbl_embarazo
lbl_fuma """
ex = Datos_personales()