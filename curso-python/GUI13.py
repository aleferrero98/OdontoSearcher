#ventanas emergentes - abrir archivos - buscador de archivos
from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:/Users/alejandro/Documents/", 
                                         filetypes=(("Ficheros de Excel", "*.xlsx"), 
                                                    ("Ficheros de C++", "*.cpp"),
                                                    ("Todos los ficheros", "*.*")))
    print(fichero) #devuelve la ruta del archivo


Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()