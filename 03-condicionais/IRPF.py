"""
  IFRN/CNAT
  Prof Galileu Batista
  Ago/2026
  
  Cálculo de IRPF
"""

print ("Cálculo de Imposto de Renda Pessoa Física")
salario = float(input("Digite o seu salário (em R$): "))
salario = round(salario, 2)

if salario <= 2428.80:
    IRPF = 0
elif salario <= 2826.65:
    IRPF = salario * 0.075 - 182.16
elif salario <= 3751.05:
    IRPF = salario * 0.15 - 394.16
elif salario <= 4664.68:
    IRPF = salario * 0.225 - 675.49
else:
    IRPF = salario * 0.275 - 908.73

if salario <= 5000:
    IRPF = IRPF - 312.89
elif salario <= 7350:
    IRPF = IRPF - (978.62 - salario*0.133145)

if IRPF < 0:
    IRPF = 0

salario_liquido = salario - IRPF

print ("Salário: ", salario)
print ("IRPF:", IRPF)
print ("Salário Líquido: ", salario_liquido)
