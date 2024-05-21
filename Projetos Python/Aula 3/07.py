#Faça um programa que peça o tamanho de um arquivo para download (em B) e a velocidade do link de internet é de 1bps, calcule e informe o tempo de download do arquivo em minutos.

download = int(input("Qual tamanho do download em Bytes: "))
download_bits = download*8

minutos = download_bits/60

print("Um arquivo de",download,"Bytes, dermora",minutos,"minutos para terminar o download.")