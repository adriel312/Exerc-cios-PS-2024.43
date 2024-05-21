matriz =[[0]*3,
         [0]*3,
         [0]*3]

for i in range(3):
    for j in range(3):
        matriz[i][j] = i*j

for i in matriz:
    print(i)