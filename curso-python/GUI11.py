#Menu en tkinter

from tkinter import *

root = Tk()
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
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

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
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")

root.mainloop()