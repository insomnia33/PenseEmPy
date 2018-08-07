def gradeline():
	print("+", end=" ") # faz os + e -
	for i in range(4):
		print("-", end=" ")
	print("+", end=" ")
	for i in range(4):
		print("-", end=" ")
	print("+")


def gradebar():	
	for i in range(4): # faz as barras
		print("|", end="         ")
		print("|", end="         ")
		print("|") 
	


n = int(input("Digite quantos andares voce quer: "))
gradeline()
	
if (n > 1):
	for i in range (1, n):
		gradebar()
		grdaeline()
		graedbar()
else:
	gradebar()

gradeline()