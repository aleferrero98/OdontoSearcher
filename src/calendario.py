from tkinter import *
from tkcalendar import *

class Calendario:
    def __init__(self, fecha):
        self.root = Tk()
        self.root.title('Calendario')
        self.root.iconbitmap('../imagenes/diente.ico')
        #root.geometry('400x400')

        self.fecha = fecha

        self.frame = Frame(self.root)
        self.frame.pack()

        self.cal = Calendar(self.frame, selectmode="day", date_pattern="dd/mm/y")
        self.cal.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        self.btn_apply = Button(self.frame, text="Aplicar", command=self.get_fecha) # el "aplicar" es solo para que te muestre la fecha
        self.btn_apply.grid(row=2, column=1, padx=5, pady=5)              # lo que importa es el OK
        self.label_fecha = Label(self.frame, text=self.cal.get_date())
        self.label_fecha.config(bg="#FFF576")
        self.label_fecha.grid(row=2, column=2, padx=5, pady=5)
        self.btn_ok = Button(self.frame, text="OK", width=10, command=self.save_fecha)
        self.btn_ok.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

    def get_fecha(self):
        self.fecha.set(self.cal.get_date())
        self.label_fecha.config(text=self.fecha.get())

    def save_fecha(self):
        self.fecha.set(self.cal.get_date()) #guarda la fecha seleccionada en la variable de control
        self.root.destroy() #cierra pop-up


#ex = Calendario()