#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve informar de qual número ele deseja ver a tabuada.

num = int(input("Informe o número que deseja ver a tabuada: "))
while num<=0 or num>10:
    num = int(input("Informe o número que deseja ver a tabuada: "))

i = 1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1