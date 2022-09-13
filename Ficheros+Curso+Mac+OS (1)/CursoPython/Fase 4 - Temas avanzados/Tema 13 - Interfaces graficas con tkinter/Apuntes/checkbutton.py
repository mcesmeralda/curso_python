from tkinter import *

def seleccionar():
    cadena = ""
    if (uzumaki.get()):
        cadena += "es uzumaki"
    else:
        cadena += " no es uzumaki"
    if (uchiha.get()):
        cadena += " y es uchiha"
    else:
        cadena += " y no es uchiha"
    monitor.config(text=cadena)

root = Tk()
root.title("naruto")
root.config(bd=15)

uzumaki = IntVar()
uchiha = IntVar() 

imagen = PhotoImage(file="naruto.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="right")

Label(frame, text="¿de que clan es naruto?").pack(anchor="w")
Checkbutton(frame, text="clan uzumaki", variable=uzumaki, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="clan uchiha", variable=uchiha, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
 
monitor = Label(frame)
monitor.pack()
root.mainloop()