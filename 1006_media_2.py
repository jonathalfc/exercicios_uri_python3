# coding: utf-8

def media(A,B,C):

	A = float(A * 2)/10
	B = float(B * 3)/10
	C = float(C * 5)/10
	MEDIA = (A+B+C)
	print('MEDIA = %.1f' %MEDIA)


A = float(input())
B = float(input())
C = float(input())

MEDIA = media(A,B,C)
