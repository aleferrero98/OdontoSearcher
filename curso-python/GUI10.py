#Checkbutton en tkinter

from tkinter import *

root = Tk()
root.title("Ejemplo")

playa = IntVar()
montania = IntVar()
turismoRural = IntVar()

def opcionesViaje():
    opcionElegida = ""

    if(playa.get() == 1):
        opcionElegida += " playa"
    if(montania.get() == 1):
        opcionElegida += " montaña"
    if(turismoRural.get() == 1):
        opcionElegida += " turismo rural"

    textoFinal.config(text=opcionElegida)

foto = PhotoImage(file="../imagenes/exit.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montania, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()