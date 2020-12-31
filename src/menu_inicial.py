import tkinter as tk
import sys

#falta:
    # agregar icono de app arriba

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
        #self.raiz.iconbitmap('/imagenes/diente.ico') #Cambiar el icono, debe ser .ico
        #self.raiz.iconbitmap(r'../OdontoSearcher/diente.ico') #Cambiar el icono 
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

        # Widgets menu
        # cuadros
        cuadro_nombre = tk.Entry(canvas_fondo, width=20)
        cuadro_nombre.config(fg="black", justify="left", font=("arial", 12))
        #imagenes
        img_lupa = tk.PhotoImage(file="../imagenes/lupa2.png")
        img_borrar = tk.PhotoImage(file="../imagenes/borrar.png", width=50, height=50)
        img_salir = tk.PhotoImage(file="../imagenes/exit.png")
        # botones
        btn_lupa = tk.Button(image = img_lupa, cursor="hand2")
        #btn_lupa["bg"] = "white"
        #btn_lupa["border"] = "0"
        btn_crear = tk.Button(text = "Crear", cursor="hand2")
        btn_borrar = tk.Button(image = img_borrar, cursor="hand2", width=50, height=50)
        btn_salir = tk.Button(image = img_salir, cursor="hand2", command=self.finalizar_programa)
        #checkbox

        # Se ubican los widgets en el canvas
        alineacion_Y = 320
        canvas_fondo.create_text(60, alineacion_Y, text="Paciente", font=("waltograph", 30))
        cuadro_window = canvas_fondo.create_window(220, alineacion_Y, window=cuadro_nombre)
        lupa_window = canvas_fondo.create_window(350, alineacion_Y, window=btn_lupa)
        crear_window = canvas_fondo.create_window(415, alineacion_Y, window=btn_crear)
        borrar_window = canvas_fondo.create_window(470, alineacion_Y, window=btn_borrar)
        salir_window = canvas_fondo.create_window(460, 23, window=btn_salir)
        #cuadro_nombre = tk.Entry(canvas_botones)
        #cuadro_nombre.grid(row=0, column=1, padx=5, pady=5)
       # tk.Button(canvas_botones, text="Clícame").pack() 

        self.raiz.mainloop()   

    def finalizar_programa(self):
        print('Byeee')
        sys.exit(0)
   # def aparecer(self):
    #    self.raiz.mainloop()    



# create the application
#app = Menu()

# start the program
#app.raiz.mainloop()