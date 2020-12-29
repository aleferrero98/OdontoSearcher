#tkinter python: text y button 
from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

#variable de control asociada a un widget
mi_name = StringVar(value="Facundo") 

#cuadro de texto de una linea
cuadroNombre = Entry(miFrame, textvariable=mi_name)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
cuadroNombre.config(fg="red", justify="center", font="waltograph")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=5, pady=5)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=5, pady=5)
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=5, pady=5)
cuadroPass.config(show="*")

#cuadro de texto largo
textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=4, column=1, padx=5, pady=5)
#barra de scroll
scroll_vertical = Scrollbar(miFrame, command=textoComentario.yview)
scroll_vertical.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scroll_vertical.set, bg="grey")

#etiquetas
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="w",  padx=5, pady=5)
passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="w",  padx=5, pady=5)
comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="w",  padx=5, pady=5)

def codigoBoton():
    mi_name.set("Alejandro")

#botones
btn_envio = Button(raiz, text="Enviar", command=codigoBoton)
btn_envio.pack()

raiz.mainloop()