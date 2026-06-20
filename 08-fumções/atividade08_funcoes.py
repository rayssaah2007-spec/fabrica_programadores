# Autor: Rayssa Ramos
# Projeto: Condicionais

# Definição de variáveis
nome = input("Digite seu nome: ")
nota = float(input('digite sua nota: '))
# Função status do aluno
def status(nota):
    if nota>= 6:
        print("Aluno aprovado! ")
    else:
        print("Aluno Reprovado!")
# Chamada da função
status(nota)


