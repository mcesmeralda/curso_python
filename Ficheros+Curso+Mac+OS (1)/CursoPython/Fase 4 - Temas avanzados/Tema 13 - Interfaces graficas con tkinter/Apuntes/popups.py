from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


root = Tk() 
def test():
    #MessageBox.showinfo("seventeen!","we are seventeen")
	#MessageBox.showwarning("Alerta!","seccion solo para administradores")
    #MessageBox.showerror("error!","ha ocurrido un error inesperado")
	#resultado = MessageBox.askquestion("salir!","¿estas seguro que deseas salir sin guardar?")
    
	#if resultado == "yes": # "no"
      
	#  root.destroy()
	#resultado = MessageBox.askokcancel("salir!","¿sobreescribir el fichero actual?")
	#resultado = MessageBox.askyesno("salir!","¿ estas seguro que deseas salir sin guardar?")
	
	#if resultado:
	#	root.destroy()
	#resultado = MessageBox.askretrycancel("reintentar", "no se puede conectar")
    
	#if resultado:
	
	#	root.destroy()
	#ColorChooser.askcolor(title= "elige un color")
	fichero = FileDialog.askopenfilename(title="abrir un fichero", "initiadir="c:""),
	      fletypes=(("fichero de texto","*.txt"),
		     (fichero de texto avanzado",*)
    
	print(fichero)

Button(root, text="Cliclame", command=test).pack()


root.mainloop()