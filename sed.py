def sed(s1, s2, f1, f2):

	file1 = open(f1, 'r')
	file2 = open(f2, 'w')
	filelist = file2.readlines()
	for line in filelist:
		if s1 == line:
			file2.write(s2)
		else:
			file2.write(s1)
	






stringpadrao = input("Digite a frase padrao: ")
stringsub = input("Digte a frase de substituicao: ")
arquivo1 = input('Digite o nome do primeiro arquivo: ')
arquivo2 = input('Digite o nome do segundo arquivo: ')

sed(stringpadrao, stringsub, arquivo1, arquivo2)