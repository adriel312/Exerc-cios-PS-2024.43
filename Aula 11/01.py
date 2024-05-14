valor = [0,7,3,1,9]
maior = 0
pos_maior = 0
menor = 0
pos_menor = 0
for i in range(5):
    if valor[i] > maior:
        maior = valor[i]
        pos_maior = i
    if valor[i] < menor:
        menor = valor[i]
        pos_menor = i
print("O maior é",maior,"e ele está na posição",pos_maior)
print("O menor é",menor,"e ele está na posição",pos_menor)