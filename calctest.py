from tkinter import *
from functools import partial

def root_specs(janela): #Propriedades da janela escolhida
	janela.title("Prontuário Eletrônico de Pacientes")
	janela["background"] = "white"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("800x600+20+20")

def root_texts(janela): #Textos contidos na janela

	global lb1
	lb1 = Label(root, text = "Calculadora: ")
	lb1.place(x = 180, y = 30)

	global lb2
	lb2 = Label(root, text = "RESULTADO")
	lb2. place(x = 400, y = 30)

def root_widgets(janela): # Botoes da respectiva janela
	
	global ed1
	ed1 = Entry(janela)
	ed1.place(x = 180, y = 50)

	global ed2
	ed2 = Entry(janela)
	ed2.place(x = 180, y = 75)

	btsoma = Button(janela, width=5, text = "+", command = bt_sum)
	btsoma.place(x = 180, y = 100)

	btsub = Button(janela, width=5, text = "-", command = bt_sub)
	btsub.place(x = 180, y = 130)

	btmult = Button(janela, width=5, text = "x", command = bt_mult)
	btmult.place(x = 250, y = 100)

	btdiv = Button(janela, width=5, text = "/", command = bt_div)
	btdiv.place(x = 250, y = 130)



def bt_sum():
	
	if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
		a = float(ed1.get())
		b = float(ed2.get())
		lb2["text"] = a + b
	else:
		lb2["text"] = "Digite apenas números"

def bt_sub():
	
	if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
		a = float(ed1.get())
		b = float(ed2.get())
		lb2["text"] = a - b
	else:
		lb2["text"] = "Digite apenas números"

def bt_mult():
	
	if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
		a = float(ed1.get())
		b = float(ed2.get())
		lb2["text"] = a * b
	else:
		lb2["text"] = "Digite apenas números"

def bt_div():
	
	if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
		a = float(ed1.get())
		b = float(ed2.get())
		lb2["text"] = a / b
	else:
		lb2["text"] = "Digite apenas números"

# MAIN, e textos da janela
root = Tk()

root_specs(root)
root_widgets(root)
root_texts(root)


root.mainloop()