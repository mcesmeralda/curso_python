from tkinter import *
from turtle import right
root = Tk()
"""
texto = StringVar()
texto.set("seventeen the best group of the generation")

Label(root, text="¡say the name seventeen!").pack(anchor="nw") 
label = Label(root, text="¡bagtang boys!")
label.pack(anchor="center")
Label(root, text="¡one a million!").pack(anchor="se")

label.config(bg="pink", fg="blue", font=("arial black",24))
label.config(textvariable=texto)
"""
imagen = PhotoImage(file="naruto.gif")
Label(root, image=imagen, bd=0).pack(side="left")






root.mainloop()

