from tkinter import *
"""
def hola():
    print("hola seventeen")

def crear_label():
    Label(root, text="seventeen el mejor grupo de la generacion").pack()
"""
def resta():
    r.set(float(n1.get()) - float(n2.get()) )
    borrar()
def suma():
    r.set(float(n1.get()) + float(n2.get()) )
    borrar()
def producto():
    r.set(float(n1.get()) * float(n2.get()) )
    borrar()
def division():
    r.set(float(n1.get()) / float(n2.get()) )
    borrar()


def borrar():
    n1.set("")
    n2.set("")
 
root = Tk()
root.config(bd=15)
n1 = StringVar()
n2 = StringVar() 
r = StringVar()
Label(root, text="numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root, text="resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()
Label(root, text="").pack()
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="suma", command=suma).pack(side="left")
Button(root, text="producto", command=producto).pack(side="left")
Button(root, text="division", command=division).pack(side="left")




root.mainloop()
