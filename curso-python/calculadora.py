from tkinter import *

raiz = Tk()
raiz.title("CASIO fx-95MS")
raiz.resizable(False,False)

frame = Frame(raiz)
frame.pack()

operacion = ""
ultimo_operando = 0
resultado = 0
hay_coma = False #flag que indica si ya se puso una coma en el numero decimal
nuevo_num = True #flag que indica un nuevo numero -> se concatenan los digitos

#-----------------pantalla----------------------
numeroPantalla = StringVar(value="0")

pantalla = Entry(frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=7, pady=7, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#-----------------pulsaciones de teclas---------------------
def numeroPulsado(num):
    global operacion
    global hay_coma
    global nuevo_num
    if(numeroPantalla.get() == "0"):
        numeroPantalla.set(num)
    elif(nuevo_num == True): #aprete tecla de operacion, guardo nuevo nro
        numeroPantalla.set(num)
        nuevo_num = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num) #concatena con digitos anteriores
    
def setComaDecimal():
    global hay_coma
    if(not hay_coma):
        hay_coma = True
        numeroPantalla.set(numeroPantalla.get() + '.')

def limpiaPantalla():
    global resultado
    global hay_coma
    global operacion
    global ultimo_operando
    numeroPantalla.set("0")
    resultado = 0
    operacion = ""
    hay_coma = False
    ultimo_operando = 0

def calcular(oper):
    global operacion
    global resultado
    global hay_coma
    global nuevo_num
    if(operacion != ""):
        resultado = operar(resultado, float(numeroPantalla.get()), operacion)
        numeroPantalla.set(resultado)
    else:
        resultado = float(numeroPantalla.get())
    operacion = oper
    hay_coma = False
    nuevo_num = True

def restar(num):
    global operacion
    global resultado
    global hay_coma
    global nuevo_num
    if(operacion != ""):
        resultado = operar(resultado, float(numeroPantalla.get()), operacion)
        numeroPantalla.set(resultado)
    else:
        resultado = float(numeroPantalla.get()) #guarda primer operando
    operacion = "resta"
    hay_coma = False
    nuevo_num = True

def multiplicar(num):
    global operacion
    global resultado
    global hay_coma
    resultado = resultado * float(num)
    operacion = "multiplicacion"
    numeroPantalla.set(resultado)
    hay_coma = False

def dividir(num):
    global operacion
    global resultado
    global hay_coma
    if(num == "0"):
        numeroPantalla.set("Syntax Error")
    else:
        resultado = resultado / float(num)
        operacion = "division"
        numeroPantalla.set(resultado)
    hay_coma = False

def mostrar_resultado():
    global resultado
    global hay_coma
    global operacion
    global ultimo_operando
    ultimo_operando = float(numeroPantalla.get())
    if(operacion == 'suma'):
        resultado = resultado+ultimo_operando
    elif(operacion == 'resta'):
        resultado = resultado-ultimo_operando
    elif(operacion == 'multiplicacion'):
        resultado = resultado*ultimo_operando
    elif(operacion == 'division'):
        resultado = resultado/ultimo_operando
    
    numeroPantalla.set(resultado)
    hay_coma = False

def operar(a, b, op):
    if(op == 'suma'):
        return a+b
    elif(op == 'resta'):
        return a-b
    elif(op == 'multiplicacion'):
        return a*b
    elif(op == 'division'):
        return a/b

#------------------fila 1------------------------
boton7 = Button(frame, text="7", width=2, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(frame, text="8", width=2, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(frame, text="9", width=2, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(frame, text="/", width=2, command=lambda:calcular("division"))
botonDiv.grid(row=2, column=4)

#------------------fila 2------------------------
boton4 = Button(frame, text="4", width=2, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(frame, text="5", width=2, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(frame, text="6", width=2, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(frame, text="X", width=2, command=lambda:calcular("multiplicacion"))
botonMult.grid(row=3, column=4)

#------------------fila 3------------------------
boton1 = Button(frame, text="1", width=2, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(frame, text="2", width=2, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(frame, text="3", width=2, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(frame, text="-", width=2, command=lambda:calcular("resta"))
botonRest.grid(row=4, column=4)

#------------------fila 4------------------------
boton0 = Button(frame, text="0", width=2, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(frame, text=",", width=2, command=lambda:setComaDecimal())
botonComa.grid(row=5, column=2)
botonClear = Button(frame, text="C", width=2, command=lambda:limpiaPantalla())
botonClear.grid(row=5, column=3)
botonSum = Button(frame, text="+", width=2, command=lambda:calcular("suma"))
botonSum.grid(row=5, column=4)
botonIgual = Button(frame, text="=", width=8, background="#E54C00", command=lambda:mostrar_resultado())
botonIgual.grid(row=6, column=1, columnspan=4)

raiz.mainloop()