#coding: utf-8

def esfera(raio):
	pi = 3.14159

	raio = raio
	raio = float(raio)
	raio = raio**3
	raio = (((4.0/3) * pi) * raio)
	
	print('VOLUME = %.3f' %raio)



raio = input()
esfera(raio)