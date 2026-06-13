#Autor: Rayssa Ramos
#Projetos: listas em Python
#           0         1         2        3         4        5
nomes = ["pelé","Maradona","messi","Ronaldo"] # Neymar # pedro 
print(*nomes)

# adicionando um nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append("pedro")
print(*nomes)

# adicionando um nome em uma posição expecífica
nomes.insert(4,"neymar")
print(*nomes)

# modificar uma pessoa da lista
nomes [5] = "Mbappe"
print(*nomes)

# removendo um nome da lista
del nomes [2]
print(*nomes)

# removendo um nome por texto
# buscar o nome e apagar o primeiro que aparecer
nomes.remove("Maradona")
print(*nomes)

# usando o pop para mostrar o nome remolvido
#   0     1      2      3
# pelé Ronaldo Neymar Mbappe
remolvido = nomes.pop(1)
print(f"Após o pop foi remolvido o nome: (remolvido)", nomes) 

