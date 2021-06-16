# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:00:40 2021

@author: daymonker
"""

from tkinter import *
from math import *
ventana = Tk()
ventana.title("Calculadora Daymonker Corporation")
ventana.geometry("400x600")
ventana.resizable(False,False)
ventana.configure(background="lightcyan")

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

raiz=Tk()

def infoAdicional():
    messagebox.showinfo("Para más información, visitar aquiyahoralatino.wordpress.com - Sitio Web - Todos los derechos reservados - Daymonker Corporation")
    
def infoLicencia():
    messagebox.showwarning("Licencia","All rights reserved - Calculator 2020-2021 - Daymonker Corporation®")

def salirApp():
    valor=messagebox.askokcancel("Salir","Estás seguro que desesa salir?")
    if valor=="True":
        raiz.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","Mo es posible cerrar el documento")
    if valor==Flase:
        raiz.destroy()
                                                    
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirApp)

edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientaMenu=Menu(barraMenu, tearoff=0)
herramientaMenu.add_command(label="Remplazar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=infoLicencia)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


color_boton="LightSkyBlue1"
ancho_boton=10
alto_boton=3
operador = ""
texto_pantalla = StringVar()
def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")
def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "ERROR"
    texto_pantalla.set(r)
    
clear()
    
#Botones de la primera fila
Boton0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(0)).grid(row=1,column=0,pady=10)
Boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(1)).grid(row=1,column=1,pady=10)
Boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(2)).grid(row=1,column=2,pady=10)
Boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(3)).grid(row=1,column=3,pady=10)
#Botones de la segunda fila
Boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(4)).grid(row=2,column=0,pady=10)
Boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(5)).grid(row=2,column=1,pady=10)
Boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(6)).grid(row=2,column=2,pady=10)
Boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(7)).grid(row=2,column=3,pady=10)
#Botones de la tercera fila
Boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(8)).grid(row=3,column=0,pady=10)
Boton9 = Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(9)).grid(row=3,column=1,pady=10)
BotonPi = Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("pi")).grid(row=3,column=2,pady=10)
BotonPunto = Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(".")).grid(row=3,column=3,pady=10)
#Botones de la cuarta fila
BotonSuma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("+")).grid(row=4,column=0,pady=10)
BotonResta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("-")).grid(row=4,column=1,pady=10)
BotonMulti = Button(ventana,text="x",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("*")).grid(row=4,column=2,pady=10)
BotonDivi = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("/")).grid(row=4,column=3,pady=10)
#Botones de la quinta fila
BotonRaiz = Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("sqrt")).grid(row=5,column=0,pady=10)
BotonClear = Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).grid(row=5,column=1,pady=10)
BotonEXP = Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("exp")).grid(row=5,column=2,pady=10)
BotonIgual = Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).grid(row=5,column=3,pady=10)
#Botones de la sexta fila
BotonParenIzq = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("(")).grid(row=6,column=0,pady=10)
BotonParenDer = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(")")).grid(row=6,column=1,pady=10)
BotonMod = Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("%")).grid(row=6,column=2,pady=10)
BotonLN = Button(ventana,text="LN",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("log")).grid(row=6,column=3,pady=10)








Pantalla = Entry(ventana,font=("arial",20,"bold"),width=22,borderwidth=10,background="CadetBlue1",textvariable=texto_pantalla)
Pantalla.grid(row=0,column=0,columnspan=4,padx=20,pady=20)


ventana.mainloop()
