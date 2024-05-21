#Faça um programa que leia três números e mostre-os em ordem crescente.
num_1 = int(input("Informe o número 1: "))
num_2 = int(input("Informe o número 2: "))
num_3 = int(input("Informe o número 3: "))

if num_1>num_2:
    temp = num_1
    num_1 = num_2
    num_2 = temp
if num_2>num_3:
    temp = num_2
    num_2 = num_3
    num_3 = temp
if num_1>num_2:
    temp = num_1
    num_1 = num_2
    num_2 = temp

print(num_1,num_2,num_3)