#Autor: Rayssa Ramos
#Projeto: listas em Python

#           0         1         2        3         4  
nomes = ["pelé","Maradona","messi","Ronaldo"] #  pedro 
print(*nomes)

# adicionando um nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append("pedro")
print(*nomes)


# removendo um nome por texto
# buscar o nome e apagar o primeiro que aparecer
nomes.remove("Maradona")
print(*nomes)