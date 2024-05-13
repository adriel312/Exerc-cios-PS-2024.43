nomes = ["Maynara", "Luiz Carlos", "Luiz Gustavo", "Arthur", "Anderson", "Gabriel", "Luana", "Higor", "Pedro", "Luiz Felipe", "Felipe"]
cont = 0
nomes.insert(7,"Adrian")

for nome in nomes:
    if nome[0] == "A":
        cont += 1

print("Haviam",cont,"nomes iniciados em A!")