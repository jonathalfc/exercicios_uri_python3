# coding: utf-8

def media(A,B):

	A = float(A * 3.5)/11
	B = float(B * 7.5)/11
	MEDIA = (A+B)
	print('MEDIA = %.5f' %MEDIA)


A = float(input())
B = float(input())

MEDIA = media(A,B)
