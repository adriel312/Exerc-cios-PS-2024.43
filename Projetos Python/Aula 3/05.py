#Faça um programa que pergunte quanto você ganha por hora e a quantidade de dias trabalhados no mês (cada dia trabalhado são 8 horas). Calcule e mostre o salário no final do mês.

dias = int(input("Quantos dias você trabalhou no mês: "))
valor_hora = float(input("Informe o valor da sua hora de trabalho: "))

horas_mes = dias * 8
salario = horas_mes * valor_hora

print("O seu salário é de: ",salario)