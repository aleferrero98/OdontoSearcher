import tkinter as tk

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
        canvas_fondo.create_text(100, 350, text="Paciente", font=("waltograph", 30))

        btn_lupa = tk.Button(text = "lupa", anchor = 'w')
        btn_crear = tk.Button(text = "Crear", anchor = 'w')
        lupa_window = canvas_fondo.create_window(300, 350, window=btn_lupa)
        crear_window = canvas_fondo.create_window(350, 350, window=btn_crear)
        #cuadro_nombre = tk.Entry(canvas_botones)
        #cuadro_nombre.grid(row=0, column=1, padx=5, pady=5)
       # tk.Button(canvas_botones, text="Clícame").pack() 

        self.raiz.mainloop()   

    
   # def aparecer(self):
    #    self.raiz.mainloop()    



# create the application
#app = Menu()

# start the program
#app.raiz.mainloop()