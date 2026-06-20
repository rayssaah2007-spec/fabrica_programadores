# Autor: Rayssa Ramos
# Projeto: Função imc

# Entrada de dados
peso =float(input("Digite seu peso:"))
altura =float(input("Digite sua altura:"))

#calculo do IMC
def calcular(peso,altura):
    imc = peso / (altura **2)
   
    #Exibindo resultado
    print(f"\nSeu IMC e:{imc:.2f}")

calcular(peso,altura)
