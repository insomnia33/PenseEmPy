from tkinter import *
from functools import partial

def root_specs(janela): #Propriedades da janela escolhida
	janela.title("Prontuário Eletrônico de Pacientes")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("800x600+300+100")

def root_texts(janela):

	global lb1
	lb1 = Label(root, fg = "Green", bg = "black", text = "Nome de Usuário: ")
	lb1.pack(anchor=N)

	global lb2
	lb2 = Label(root, fg = "Green", bg = "black", text = "RESULTADO")

def root_widgets(janela): # Botoes da respectiva janela
	
	global ed1
	ed1 = Entry(janela, fg = "Green", bg = "black")
	ed1.pack(anchor=N)

	global ed2
	ed2 = Entry(janela, fg = "Green", bg = "black")
	ed2.pack(anchor=N)

	bt1 = Button(janela, width=15, text = "SOMA", bg ="Black", fg = "Green",  command = bt_onclick)
	bt1.pack(anchor=N)

	lb2.pack(anchor=N)


def bt_onclick():
	
	if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
		a = float(ed1.get())
		b = float(ed2.get())
		lb2["text"] = a + b
	else:
		lb2["text"] = "Digite apenas números"


# MAIN, e textos da janela
root = Tk()

root_specs(root)
root_texts(root)
root_widgets(root)



root.mainloop()