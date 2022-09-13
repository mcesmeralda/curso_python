from tkinter import *
root = Tk()
 
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu=(menubar, tearoff=0)
filemenu.add_commnand(label="new")
filemenu.add_commnand(label="open")
filemenu.add_commnand(label="save")
filemenu.add_commnand(label="close")
filemenu.add_separator()
filemenu.add_commnand(label="exit", command=root.quit)

editmenu = Menu=(menubar, tearoff=0) 
filemenu.add_commnand(label="copy")
filemenu.add_commnand(label="paste") 
filemenu.add_commnand(label="cut")

helpmenu = Menu=(menubar, tearoff=0)
filemenu.add_commnand(label="help")
filemenu.add_separator()
filemenu.add_commnand(label="acerca de ...")



menubar.add_cascade(label="file", menu=filemenu)
menubar.add_cascade(label="edit", menu=editmenu)
menubar.add_cascade(label="help", menu=helpmenu)

root.mainloop()

