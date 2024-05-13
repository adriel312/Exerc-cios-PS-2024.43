'''Suponha que você está desenvolvendo o sistema de um hotel que deve abrir um menu de opções para o cliente, as opções dele, são:
1. Fazer Check-in
2. Chamar serviço de quarto
3. Fazer pedido
4. Fazer Check-out'''

print("1. Fazer Check-in")
print("2. Chamar serviço de quarto")
print("3. Fazer pedido")
print("4. Fazer Check-out")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Check-in realizado com sucesso!")
    case 2:
        print("Serviço de quarto acionado!")
    case 3:
        print("Pedido realizado com sucesso!")
    case 4:
        print("Check-out realizado com sucesso!")
    case _:
        print("Opção selecionada é inválida!")