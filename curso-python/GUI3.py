from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack() #agrega el Frame al root, el tamaño al que se ajusta es al del frame

miImagen = PhotoImage(file="../imagenes/wallpaper.png")

miLabel = Label(miFrame, image=miImagen)
#miLabel = Label(miFrame, text="Esta es una etiqueta", fg="red", font=("Comic Sans MS", 20))
#miLabel.pack()
miLabel.place(x=0, y=0)
#miLabel.place(x=100, y=100) #ubica la etiqueta pero usa el tamaño del frame, x e y son distancia en pixeles.

root.mainloop()
