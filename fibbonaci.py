def fibo(x):
	a = 1
	b = a
	while a < x:
		c = a
		a = a + b
		b = c
		print (b, " ")

a = int(input("Digite um numero inteiro: "))
fibo(a)

