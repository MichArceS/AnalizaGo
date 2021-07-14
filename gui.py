from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from analizadorSintactico import parser
import logging

window = Tk()

style = ttk.Style(window)
window.tk.call('source','theme/azure dark/azuredark.tcl')
style.theme_use('azure')
window.title("AnalizaGo")

window.geometry('700x600')

frame = ttk.Frame(window)
lbl = ttk.Label(frame, text="Ingrese el código de go a analizar: ")
title = ttk.Label(frame,text="ANALIZA GO", font=('Helvetica',24,'bold'))

title.grid(column=0,row=0, columnspan=2)
lbl.grid(column=0, row=1, columnspan=2)

txt = Text(frame,width=60, background="white", font=('Consolas'), fg="black")

txt.grid(column=0,row=2, columnspan=2)

frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def clicked():
    ent = txt.get(1.0,END)
    print('> ' + ent)
    try:
        res = parser.parse(ent)
        messagebox.showinfo('Correcto', 'Analisis completo - Sin problemas')
    except SyntaxError as e:
        messagebox.showerror('ERROR!', e.msg)

def clear():
    txt.delete(1.0,END)
    
btnGO = ttk.Button(frame, text="GO", command=clicked)
btnCLEAR = ttk.Button(frame, text="Clear", command=clear)

btnGO.grid(column=0, row=3, pady=12)
btnCLEAR.grid(column=1,row=3,pady=12)

window.mainloop()