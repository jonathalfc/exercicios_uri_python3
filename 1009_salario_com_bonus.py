#coding: utf-8

def salario_com_bonus(nome,salario_fixo,total_vendas_no_mes):
	nome                = nome
	salario_fixo        = salario_fixo
	total_vendas_no_mes = total_vendas_no_mes
	
	total = ((total_vendas_no_mes*15)/100 + salario_fixo)
	print('TOTAL = R$ %.2f' %total)

nome                = input()
salario_fixo        = float(input())
total_vendas_no_mes = float(input())

salario_com_bonus(nome,salario_fixo,total_vendas_no_mes)