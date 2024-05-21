#Declare uma matriz para armazenar o nome dos colegas presentes em aula, com as linhas e colunas conforme a posição dos mesmos. Ao final imprima os elementos.
alunos = [["Felipe","Luiz Felipe","","Adriel"],
          ["Pedro","Higor","Gil","Maynara"],
          ["","Adrian","Luiz Carlos","Luiz Gustavo"],
          ["","Gabriel","","Arthur"],
          ["","","Anderson",""]
        ]

for i in range(len(alunos)):
    for j in range(len(alunos[0])):
        print(alunos[i][j])
    print("-------")

for i in range(len(alunos)):
    print(alunos[i])
