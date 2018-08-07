def converter():
	minutos = int(input("Digite os mintuos de duração do filme ou 0 para sair: "))
	if (minutos != 0):
		horas = minutos // 60
		resto = minutos - horas*60
		print("O filme possui duração de: %dh%dm" % (horas, resto))
		converter()
	
	


converter()
