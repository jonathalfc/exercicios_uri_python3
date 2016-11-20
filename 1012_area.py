#coding: utf-8


def area_triango(base,altura):
	base   = base
	altura = altura
	area   = (base * altura)/2
	print('TRIANGULO: %.3f' %area)


def area_circulo(raio):
	pi   = 3.14159
	raio = raio**2
	area = float(raio * pi)
	print('CIRCULO: %.3f' %area)

def area_trapezio(A,B,C):
	A = A
	B = B
	C = C
	area = (((A+B) * C) / 2)
	print('TRAPEZIO: %.3f' %area)

def area_quadrado(lado_do_quadrado):
	lado_do_quadrado = lado_do_quadrado
	area             = lado_do_quadrado**2
	print('QUADRADO: %.3f' %area)


def area_retangulo(lado_a,lado_b):
	lado_a = lado_a
	lado_b = lado_b
	area   = (lado_a * lado_b)
	print('RETANGULO: %.3f' %area)



valores = input("").split(" ")
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])


area_triango(A,C)
area_circulo(C)
area_trapezio(A,B,C)
area_quadrado(B)
area_retangulo(A,B)