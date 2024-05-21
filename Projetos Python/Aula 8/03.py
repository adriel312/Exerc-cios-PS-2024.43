#Faça um programa que solicita um login e senha do usuário e verifique se a senha digitada é igual ao login. Caso a senha informada seja igual ao login, solicite uma nova senha.

login = input("Informe seu login: ")
senha = input("Informe sua senha: ")
while senha == login:
    print("A senha informada não pode ser igual ao login!")
    senha = input("Informe uma nova senha: ")

print("Cadastro realizado!")