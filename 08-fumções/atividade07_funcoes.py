# Autor: Rayssa Ramos 
# Projeto: Função imc

# Declaração de variáveis
peso = float(input("Digite o seu peso: "))
altura =  float(input("Digite sua altura: "))

def calcular(peso,altura):
    imc = peso / (altura * altura)
    print(f"seu IMC é: {imc:.2f}")

calcular(peso, altura)