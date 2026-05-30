#Autor: Rayssa Ramos
#Projeto: Loop For - variáveis de inicio e fim

numero = int(input("Digite a tabuada desejada: "))
numero inicio = int(input("Digite o inicio da tabuada: "))
numero_fim = int(input("Digite o fim da tabuada: "))

#loop For
for i in range (1,11):
    print(f'{numero} x {i} = {i * numero}')
