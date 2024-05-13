nota_1 = float(input("Informe a nota 1: "))
nota_2 = float(input("Informe a nota 2: "))

media = (nota_1+nota_2)/2

if media>=7:
    print("Aprovado")
elif media>=5:
    print("Recuperação")
else:
    print("Reprovado")