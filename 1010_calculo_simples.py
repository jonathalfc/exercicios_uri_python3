#coding: utf-8


def calculo_simples(quantidade,valor_unitario):

	quantidade                = quantidade
	valor_unitario            = valor_unitario
	
	total_peca                = float(quantidade * valor_unitario)
	
	return total_peca


def soma_compra(total_peca_1,total_peca_2):
	total_peca_1 = total_peca_1
	total_peca_2 = total_peca_2

	total_compra = (total_peca_1 + total_peca_2)
	print('VALOR A PAGAR: R$ %.2f' %total_compra)



valores = input("").split(" ")

codigo_peca    = int(valores[0])
quantidade     = int(valores[1])
valor_unitario = float(valores[2])

total_peca_1 = calculo_simples(quantidade,valor_unitario)



valores2 = input("").split(" ")

codigo_peca2    = int(valores2[0])
quantidade2     = int(valores2[1])
valor_unitario2 = float(valores2[2])


total_peca_2 = calculo_simples(quantidade2,valor_unitario2)

soma_compra(total_peca_1,total_peca_2)
