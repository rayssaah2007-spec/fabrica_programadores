#autor: Rayssa Ramos
#Entrada de dados
peso =float(input("Digite seu peso:"))
altura =float(input("Digite sua altura:"))

#calculo do IMC
imc = peso / (altura **2)

#Exibindo resultado
print(f"\nSeu IMC e:{imc:..2f}")

#Classificacao
if imc< 18.5:
    print("Abaixo do peso")
    
elif imc <25:
    print("Peso normal")

elif imc <30:
    print("Sobrepeso")

else:
    print("Obesidade")    