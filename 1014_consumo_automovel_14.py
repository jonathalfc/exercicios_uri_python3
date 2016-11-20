#coding: utf-8

def consumo(distancia, combustivel):
	distancia   = distancia
	combustivel = combustivel
			
	media = (distancia/combustivel)
	media = round(media,3)
	texto = " km/l"
	print(repr(media) + texto)
	



distancia   = input()
combustivel = input()

distancia   = int(distancia)
combustivel = float(combustivel)

combustivel = round(combustivel,1)

consumo(distancia,combustivel)


