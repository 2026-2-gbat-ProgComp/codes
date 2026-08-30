"""
  IFRN/CNAT
  Prof Galileu Batista
  Ago/2026
  
  Cálculo raízes de equação do 2o grau
  Ignorando casos especiais
"""

print ("Cálculo raízes de equação do 2o grau")
a = int(input("Coeficiente a: "))
b = int(input("Coeficiente b: "))
c = int(input("Coeficiente c: "))

delta = b*b - 4*a*c
x1 = (-b + delta**(1/2))/(2*a)
x2 = (-b - delta**0.5)/(2*a)

print ("Raízes: ", x1, "e", x2)