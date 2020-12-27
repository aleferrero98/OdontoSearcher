#entry tkinter python
from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
cuadroNombre.config(fg="red", justify="center", font="waltograph")
#cuadroTexto.pack()
#cuadroTexto.place(x=100, y=200)
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=5, pady=5)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=5, pady=5)
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=5, pady=5)
cuadroPass.config(show="*")

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="w",  padx=5, pady=5)
passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="w",  padx=5, pady=5)

raiz.mainloop()
