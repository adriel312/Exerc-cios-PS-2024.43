#Faça um programa que verifique se o sexo do usuário é F-Feminino e M-Masculino. Confirme e escreva o sexo digitado pelo usuário.

sexo = input("Informe seu sexo, M-Masculino F-Feminino ")

if sexo == "f":
    print("Feminino")
elif sexo == "m":
    print("Masculino")
else:
    print("Valor não identificado!")