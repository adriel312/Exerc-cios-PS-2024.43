#Faça um programa que peça dois números e imprima o maior deles.
num_1 = int(input("Informe o número 1: "))
num_2 = int(input("Informe o número 2: "))

if num_1>num_2:
    print(num_1)
elif num_1<num_2:
    print(num_2)
else:
    print("Os números são iguais!")