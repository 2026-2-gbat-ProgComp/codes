"""
  IFRN/CNAT
  Prof Galileu Batista
  Ago/2026
  
  Cálculo e classificação do IMC
"""

print ("Cálculo e classificação do IMC")
peso = float(input("Digite o seu peso (em Kg): "))
altura = float(input("Digite a sua altura (em m): "))
IMC = round(peso / altura**2, 1)

if IMC < 18.5:
    classe = "Abaixo do peso"
elif IMC <= 24.9:
    classe = "Peso normal"
elif IMC <= 29.9:
    classe = "Sobrepeso"
elif IMC <= 34.9:
    classe = "Obesidade Grau I"
elif IMC <= 39.9:
    classe = "Obesidade Grau II"
else:
    classe = "Obesidade Grau III (mórbida)"

print ("Seu IMC é ", IMC, ", que é classificado como '", 
       classe, "'", sep="")
