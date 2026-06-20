# Autor: Rayssa Ramos
# Projeto: Entrada pelo usuário

# Entrada de dados
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor'))

# Função calcular 
def calcular (valor1,valor2):
    somar = valor1+valor2
    subtrair = valor1-valor2
    multiplicar = valor1*valor2
    dividir = valor1/valor2

    # Imprimindo os resultados
    print(f"o resultado da soma é: {somar}")
    print(f"o resultado da subtração é: {subtrair}")
    print(f"o resultado da multiplicação é: {multiplicar}")
    print(f"o resultado da divisão é: {dividir}")

# Chamada da Função
calcular(valor1,valor2)

