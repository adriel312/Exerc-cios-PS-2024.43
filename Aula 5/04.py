#Faça um programa que peça ao usuário dois números. Depois solicite a ele qual operação aritmética deseja realizar (soma +, subtração -, multiplicação *, divisão /). No fim imprima o resultado da operação solicitada.

num_1 = int(input("Informe o valor de número 1: "))
num_2 = int(input("Informe o valor de número 2: "))

op = input("Informe a operação que deseja realizar: ")

match op:
    case "+":
        print("A soma de",num_1,"+",num_2,":", num_1+num_2)
    case "-":
        print("A soma de",num_1,"-",num_2,":", num_1-num_2)    
    case "*":
        print("A soma de",num_1,"*",num_2,":", num_1*num_2)
    case "/":
        print("A soma de",num_1,"/",num_2,":", num_1/num_2)
    case _:
        print("Operação inválida!")