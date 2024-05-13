vetor_nomes = ["Mayara", "Luiz", "Luiz", "Arthur", "Anderson", "Luana","Higor","Pedro","Luiz","Felipe"]

#print(vetor_nomes[3])
vetor_nomes[0] = "Maynara"
#print(vetor_nomes[0])

#vetor_nomes.append("Gabriel")   #adicionar valor no final da lista/vetor
vetor_nomes.insert(5,"Gabriel")
#vetor_nomes.remove("Gabriel")
valor_removido = vetor_nomes.pop(7)

for i in vetor_nomes:
    print(i)

print("Elemento removido: ",valor_removido)
ocorrencias = vetor_nomes.count("Luiz")
print("Quantas vezes apareceu o nome Luiz?",ocorrencias)
print("O vetor nomes possui",len(vetor_nomes),"nomes")