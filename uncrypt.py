def crypt(word, rot):
	newword = ""
	for i in range (len(word)):
		x = ord(word[i]) - rot
		newword = newword + chr(x)
	return newword

a = input("Digite a palavra desejada: ")
b = int(input("Digite a chave: "))

print (crypt(a, b))