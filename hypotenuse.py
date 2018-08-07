from math import *

def hypotenuse(b, c):
	a = sqrt(b**2 + c**2)
	return a

oposto = float(input("Insira o cateto oposto: "))
adjacente = float(input("Insira o cateto adjacente: "))

print ("A hipotenusa é: %.1f" % (hypotenuse(oposto, adjacente))) 