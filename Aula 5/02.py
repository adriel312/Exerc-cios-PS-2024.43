#Crie um programa que solicita o sexo do usuário. Caso ele informe F apresente a mensagem "Sexo Feminino", caso ele informe M, "Sexo Masculino". Caso informe alguma outra opção, "Sexo não definido".
sexo = input("Iforme seu sexo: ").upper()

#lower() = transforma todo texto em minusculo
#upper() = transforma todo texto em maiusculo    

match sexo:
    case "F":
        print("Sexo Feminino")
    case "M":
        print("Sexo Masculino")
    case _:
        print("Sexo não definido!")