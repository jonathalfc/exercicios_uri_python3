
def calculaArea(raio):
	pi = 3.14159
	raio = raio**2
	raio = float(raio * pi)
	return print('A=%.4f'%raio)


raio = float(input())
calculaArea(raio)