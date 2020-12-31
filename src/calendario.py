from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Calendario')
root.iconbitmap('../imagenes/diente.ico')
#root.geometry('400x400')

fecha_nac = StringVar(value="")

frame = Frame(root)
frame.pack()

cal = Calendar(frame, selectmode="day", date_pattern="dd/mm/y")
cal.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

def get_fecha():
    fecha_nac.set(cal.get_date())
    label_fecha.config(text=fecha_nac.get())

def save_fecha():
    fecha_nac.set(cal.get_date()) #guarda la fecha seleccionada en la variable de control
    root.destroy() #cierra pop-up

btn_apply = Button(frame, text="Aplicar", command=get_fecha) # el "aplicar" es solo para que te muestre la fecha
btn_apply.grid(row=2, column=1, padx=5, pady=5)              # lo que importa es el OK
label_fecha = Label(frame, text=cal.get_date())
label_fecha.config(bg="#FFF576")
label_fecha.grid(row=2, column=2, padx=5, pady=5)
btn_ok = Button(frame, text="OK", width=10, command=save_fecha)
btn_ok.grid(row=3, column=1, columnspan=2, padx=5, pady=5)


root.mainloop()