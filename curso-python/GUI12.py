#Ventanas emergentes en tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo("Odonto Searcher", "Buscador de historias clinicas - version 2021")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirApp():
    #Si - No
    valor = messagebox.askquestion("Salir", "¿Desea Salir de la aplicación?")
    print(valor)
    if(valor == "yes"):
        root.destroy()

def cerrarVentana():
    #Aceptar - Cancelar
    valor = messagebox.askokcancel("Cerrar", "¿Desea guardar los cambios antes de salir?")
    print(valor)
    if(valor == True):
        root.destroy()

def guardarDoc():
    valor = messagebox.askretrycancel("Reintentar", "No es posible guardar. Documento bloqueado.")
    print(valor)
    if(valor == True):
        guardarDoc()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=False)
archivoEdicion = Menu(barraMenu, tearoff=False)
archivoHerramientas = Menu(barraMenu, tearoff=False)
archivoAyuda = Menu(barraMenu, tearoff=False)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

archivoMenu.add_command(label="Nuevo archivo")
archivoMenu.add_command(label="Abrir archivo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar", command=guardarDoc)
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarVentana)
archivoMenu.add_command(label="Salir", command=salirApp)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_separator()
archivoEdicion.add_command(label="Deshacer")
archivoEdicion.add_command(label="Rehacer")

archivoHerramientas.add_command(label="Ejecutar")
archivoHerramientas.add_command(label="Debuggear")
archivoHerramientas.add_command(label="Abrir Configuración")
archivoHerramientas.add_command(label="Abrir Terminal")

archivoAyuda.add_command(label="Documentación")
archivoAyuda.add_command(label="Tips y ayudas")
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)

root.mainloop()
