"""
  IFRN/CNAT
  Prof Galileu Batista
  Ago/2026
  
  Cálculo de aprovação no IFRN
"""

print ("Cálculo de Aprovação no IFRN")
N1 = int(input("Digite a nota do 1o. bimestre (0 a 100): "))
N2 = int(input("Digite a nota do 2o. bimestre (0 a 100): "))

MD = (2*N1 + 3*N2)//5

if MD >= 60:
    print ("Aprovado por média e nota: ", MD)
elif MD >= 20:
    NAF = int(input("Digite a nota da prova final (0 a 100): "))
    MF1 = (MD+NAF)//2
    MF2 = (2*NAF + 3*N2)//5
    MF3 = (2*N1 + 3*NAF)//5
    
    if MF1 > MF2:
        MF = MF1
    else:
        MF = MF2

    if MF3 > MF:
        MF = MF3

    if MF >= 60:
        print ("Aprovado por nota final com ", MF)    
    else:
        print ("Reprovado após prova final com", MF)
else:
    print ("Reprovado com", MD)
