#Autor: Rayssa Ramos 
#Projeto: listas em Python

  #        0         1        2       3
nomes = ["Marlene","Aurora","Lorena","Isaac"]
print(*nomes)

nomes.append(input("Digite o nome do contato a ser adicionado"))
print(*nomes)

nomes.remove(input("Digite o contato a ser remolvido"))
print(*nomes)