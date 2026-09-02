"""
  IFRN/CNAT
  Prof Galileu Batista.
  Ago/2026
  Cédulas a dispensar para um saque em ATM
"""

print ("Saque em Caixa Eletrônico")
saque = int(input("Qual o valor desejado: "))

cedulas200 = saque // 200
saque = saque % 200
print ("# cédulas 200:", cedulas200)

cedulas100 = saque // 100
saque = saque % 100
print ("# cédulas 100:", cedulas100)

cedulas50 = saque // 50
saque = saque % 50
print ("# cédulas 50:", cedulas50)

cedulas20 = saque // 20
saque = saque % 20
print ("# cédulas 20:", cedulas20)

cedulas10 = saque // 10
saque = saque % 10
print ("# cédulas 10:", cedulas10)

cedulas5 = saque // 5
saque = saque % 5
print ("# cédulas 5:", cedulas5)

cedulas2 = saque // 2
saque = saque % 2
print ("# cédulas 2:", cedulas2)

print ("# moedas de 1:", saque)
