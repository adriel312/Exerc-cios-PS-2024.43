#Faça um programa para calcular o fatorial de um número n.
n = int(input("Informe o número que desaja o fatorial: "))
fatorial = n
for i in range(n-1,1,-1):
    fatorial = fatorial*i
print(fatorial)