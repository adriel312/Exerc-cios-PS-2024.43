#Altere o programa anterior para que ele informe a posição do maior elemento (linha e coluna) do maior.
#Leia uma matriz 3 x 3, conte e escreva quantos valores maiores que 10 ela possui.
matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]
          ]
matriz = [[0]*3,
          [0]*3,
          [0]*3
         ]
maior = 0
linha = 0
coluna = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f"Informe um valor para matriz[{i}][{j}]: "))
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j
print("O maior valor é",maior,"ele está na posição",linha,coluna)

