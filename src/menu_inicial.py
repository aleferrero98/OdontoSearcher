import tkinter as tk
import sys

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

        # Variables Control
        historia_clinica = tk.IntVar()
        odontograma = tk.IntVar()


        # Widgets menu
        # cuadros
        cuadro_nombre = tk.Entry(canvas_fondo, width=20)
        cuadro_nombre.config(fg="black", justify="left", font=("arial", 12))
        #imagenes
        img_lupa = tk.PhotoImage(file="../imagenes/lupa2.png")
        img_borrar = tk.PhotoImage(file="../imagenes/borrar.png", width=50, height=50)
        img_salir = tk.PhotoImage(file="../imagenes/exit.png")
        img_crear = tk.PhotoImage(file="../imagenes/crear.png", width=50, height=50)
        # botones
        btn_lupa = tk.Button(canvas_fondo, image = img_lupa, cursor="hand2")
        btn_crear = tk.Button(canvas_fondo, image = img_crear, cursor="hand2", width=50, height=50)
        btn_borrar = tk.Button(canvas_fondo, image = img_borrar, cursor="hand2", width=50, height=50)
        btn_salir = tk.Button(canvas_fondo, image = img_salir, cursor="hand2", command=self.finalizar_programa)
        #checkbox
        check_hist = tk.Checkbutton(canvas_fondo, text="Historia Clínica", variable=historia_clinica, onvalue=1, offvalue=0)#, command=opcionesViaje)
        check_odont = tk.Checkbutton(canvas_fondo, text="Odontograma", variable=odontograma, onvalue=1, offvalue=0)#, command=opcionesViaje)

        # Se ubican los widgets en el canvas
        alineacion_Y = 320
        canvas_fondo.create_text(60, alineacion_Y, text="Paciente", font=("waltograph", 30))
        cuadro_window = canvas_fondo.create_window(220, alineacion_Y, window=cuadro_nombre)
        lupa_window = canvas_fondo.create_window(350, alineacion_Y, window=btn_lupa)
        crear_window = canvas_fondo.create_window(411, alineacion_Y, window=btn_crear)
        borrar_window = canvas_fondo.create_window(470, alineacion_Y, window=btn_borrar)
        salir_window = canvas_fondo.create_window(460, 23, window=btn_salir)
        hist_clinica_window = canvas_fondo.create_window(150, 370, window=check_hist)
        odonto_window = canvas_fondo.create_window(300, 370, window=check_odont)

        self.raiz.mainloop()   

    def finalizar_programa(self):
        print('Byeee')
        sys.exit(0)
