print("M - Masculino")
print("F - Feminino")
sexo = input("Informe o seu sexo: ")

match sexo:
    case "M":
        altura = float(input("Informe sua altura: "))
        if altura>=1.70:
            print("Apto ao alistamento!")
        else:
            print("Inapto ao alistamento!")
    case "F":
        altura = float(input("Informe sua altura: "))
        if altura>=1.60:
            print("Apto ao alistamento!")
        else:
            print("Inapto ao alistamento!")
    case _:
        print("Valor não encontrado!")