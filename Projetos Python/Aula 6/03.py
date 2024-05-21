print("1 - Converter de Celsius para Fahrenheit")
print("2 - Converter de Fahrenheit para Celsius")

opcao = int(input("Selecione a opção de conversão: "))

match opcao:
    case 1:
        temp = float(input("Informe a temperatura em C°: "))
        print(temp,"C° equivalem a",(temp * 9/5) + 32,"F.")
    case 2:
        temp = float(input("Informe a temperatura em F: "))
        print(temp,"F equivalem a",(temp - 32) * 5/9,"C°.")
    case _:
        print("Opção inválida!")