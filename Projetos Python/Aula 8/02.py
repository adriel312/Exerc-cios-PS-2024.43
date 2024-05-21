#Faça um programa que peça duas notas, entre 0 e 10. Caso o usuário informe uma nota inválida, peça para que ele insira uma nova nota.
print("Insira notas entre 0 e 10")

nota_1 = float(input("Informe o valor de nota 1: "))
while nota_1<0 or nota_1>10:
    print("Você informou uma nota inválida!")
    nota_1 = float(input("Informe um novo valor de nota 1: "))

nota_2 = float(input("Informe o valor de nota 2: "))
while nota_2<0 or nota_2>10:
    print("Você informou uma nota inválida!")
    nota_2 = float(input("Informe um novo valor de nota 2: "))