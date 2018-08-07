def is_palindromo(a):
	b = a[::-1]
	return a == b

palavra = input("Digite uma palavra: ")

print (is_palindromo(palavra))