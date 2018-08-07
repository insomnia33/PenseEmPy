import math

class Point:
	pass

blank = Point()
blank.x = float(input("Digite um ponto: "))
blank.y = float(input("Digite outro ponto: "))
distance = math.sqrt(blank.x ** 2 + blank.y	** 2)
print("%.2f" %distance)