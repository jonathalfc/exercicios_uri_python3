#coding: utf-8

def diferenca(A,B,C,D):

	A = int(A)
	B = int(B)
	C = int(C)
	D = int(D)
	DIFERENCA = ((A*B) - (C*D))
	print('DIFERENCA = %d' %DIFERENCA)


A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = diferenca(A,B,C,D)
