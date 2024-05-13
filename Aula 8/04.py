nome = input("Informe seu nome: ")
while len(nome) < 2:
    print("Nome deve possuir mais que 2 caracteres!")
    nome = input("Informe seu nome novamente: ")
idade = int(input("Informe sua idade: "))
while idade<0 or idade>120:
    print("Idade deve estar entre 0 e 120")
    idade = int(input("Informe sua idade novamente: "))
salario = float(input("Informe o salário: "))
while salario<0:
    print("Salário não pode ser menor que 0")
    salario = float(input("Informe o salário novamente: "))
sexo = input("Informe seu sexo: ")
while sexo!="F" and sexo!="M":
    print("O sexo deve ser F ou M")
    sexo = input("Informe seu sexo novamente: ")
estado_civil = input("Informe seu estado civil: ")
while estado_civil!="s" and estado_civil!="v" and estado_civil!="s" and estado_civil!="d":
    print("Estado civil deve ser s v c ou d")
    estado_civil = input("Informe seu estado civil novamente: ")

print("Todas informações cadastradas!")