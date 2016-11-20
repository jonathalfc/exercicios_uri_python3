#coding: utf-8

def funcao_abs(valor1,valor2,valor3):
	valor1 = valor1
	valor2 = valor2
	valor3 = valor3

	maior_ab   = (a+b+abs(a-b))/2
	maior_ab_c = (maior_ab+c+abs(maior_ab-c))/2

	print('%d eh o maior'%maior_ab_c)


valores = input("").split(" ")

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

funcao_abs(a,b,c)


