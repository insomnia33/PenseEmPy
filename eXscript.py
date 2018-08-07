from tkinter import *

def janela2():
	root2 = Tk()
	root2.geometry("500x300+200+100")
	root2.mainloop()

root = Tk()	

lb1 = Label(root, text="Linha1")
lb2 = Label(root, text="Linha2")


lb1.grid(row=2, column=2)
lb2.pack(anchor=N)

root["bg"] = "white"
root.geometry("400x300+200+100")
root.mainloop()

