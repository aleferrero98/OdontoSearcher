from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(True,False)
#raiz.iconbitmap("diente.ico") #debe ser .ico
raiz.geometry("1000x350")
raiz.config(bg="blue")

miFrame = Frame()
miFrame.pack(side="left", anchor="s") # se agrega a la raiz
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="yellow")
#se le da tamaño al frame ya que la raiz se ajusta al tamaño del frame
miFrame.config(width="100",height="100")
miFrame.config(bd=15) #ancho del borde
miFrame.config(relief="sunken") #forma del borde
miFrame.config(cursor="hand2")

raiz.mainloop()
