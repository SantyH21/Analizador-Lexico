import tkinter as tk
from tkinter import ttk as ttk

from Simbolo import Simbolo

#metodo llenar la tabla

def LlenarTabla():
  
    lista = Simbolo.crearLista()
    for (token,lexema,palabraReservada) in lista:
        print(lista)

#gui tabla

root = tk.Tk()
root.geometry('600x600')
root.geometry("+400+100")
root.title("Ventana Simbolos")
root.resizable(True, True)
# Simbolos=tk.Text(root, font=("Italic", 15))
# Simbolos.place(relx=0.01, rely=0.05,relwidth=0.98, relheight=0.9)
Boton_prueba=tk.Button(root, text="Cargar tabla", font=("Italic", 15), bg="LightSkyBlue1", command=LlenarTabla)
Boton_prueba.pack()


tabla = ttk.Treeview(root, columns = ('#1','#2','#3'))
tabla.heading('#0',text='token',anchor='center')
tabla.heading('#1',text='Lexema',anchor='center')
tabla.heading('#2',text='Palabra Reservada',anchor='center')

tabla.pack()


root.mainloop()