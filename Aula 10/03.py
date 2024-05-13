#Leia uma matriz 3 x 3, conte e escreva quantos valores maiores que 10 ela possui.
matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]
          ]
matriz = [[0]*3,
          [0]*3,
          [0]*3
         ]
cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f"Informe um valor para matriz[{i}][{j}]: "))
        if matriz[i][j] > 10:
            cont += 1
print("Existem",cont,"valores maiores que 10!")