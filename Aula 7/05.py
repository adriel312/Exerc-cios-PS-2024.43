#Faça um programa que solicite ao usuário 5 números e conte os maiores que 10.
cont = 0
for i in range(5):
    num = int(input("Informe o valor: "))
    if num>10:
        cont += 1
print("Haviam",cont,"números maiores que 10")