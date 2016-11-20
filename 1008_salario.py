#coding: utf-8

def salario(numero,horas_trabalhadas,valor_hora):
	salario            = 0.0
	numero             = numero
	horas_trabalhadas  = horas_trabalhadas
	valor_hora         = valor_hora

	salario            = (horas_trabalhadas * valor_hora)
	
	print('NUMBER = %d' %numero)
	print('SALARY = U$ %.2f' %salario)


numero            = int(input())
horas_trabalhadas = int(input())
valor_hora        = float(input())

salario(numero,horas_trabalhadas,valor_hora)