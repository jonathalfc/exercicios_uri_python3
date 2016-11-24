#coding: utf-8

def distancia_entre_dois_pontos(x1,y1,x2,y2):
	x1 = x1
	x2 = x2
	y1 = y1
	y2 = y2

	distancia = (((x2 - x1)**2) + ((y2 -y1)**2))
	return distancia


def raiz_quadrada(raiz):
	raiz  = raiz
	raiz  = (raiz**(1/2.0))
	print("%.4f" %raiz)


distancia_do_eixo_xy1 = input("").split(" ")
x1 = float(distancia_do_eixo_xy1[0])
y1 = float(distancia_do_eixo_xy1[1])
	

distancia_do_eixo_xy2 = input("").split(" ")
x2 = float(distancia_do_eixo_xy2[0])
y2 = float(distancia_do_eixo_xy2[1])

calculo_distancias = distancia_entre_dois_pontos(x1,y1,x2,y2)

raiz_quadrada(calculo_distancias)