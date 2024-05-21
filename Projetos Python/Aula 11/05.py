matriz_1 = [[1,4,5,7],
            [3,6,8,1],
            [4,2,1,8],
            [7,3,12,61]]

matriz_2 = [[23,21,56,21],
            [43,253,54,243],
            [243,21,56,243],
            [243,56,51,5]]

matriz_3 = [[0]*4,
            [0]*4,
            [0]*4,
            [0]*4]

for i in range(4):
    for j in range(4):
        if matriz_1[i][j] > matriz_2[i][j]:
            matriz_3[i][j] = matriz_1[i][j]
        else:
            matriz_3[i][j] = matriz_2[i][j]

for i in matriz_3:
    print(i)