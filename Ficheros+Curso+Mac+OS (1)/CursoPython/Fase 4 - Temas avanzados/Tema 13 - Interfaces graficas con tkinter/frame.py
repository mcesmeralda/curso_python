from tkinter import *

root= Tk()
root.title("hola mundo")
root.resizable(1,1)
root.iconbitmap("hola.ico")


Frame = Frame(root, width=480, height=320)
Frame.pack(fill="both", expand=1) 
Frame.config(cursor="pirate")
Frame.config(bg="pink")
Frame.config(bd=20)
Frame.config(relief="sunken")

root.config(cursor="heart")
root.config(bg="lightblue")
root.config(bd=15)
root.config(relief="ridge")






root.mainloop()
 
    