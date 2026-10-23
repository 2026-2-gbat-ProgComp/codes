dados = """Galileu Batista#5,0#2,5;Maria Candida Xavier#8#5;Damiao Pedro#7,5#8"""

for pessoa in dados.split(";"):
    #print (pessoa)
    dados_pessoa = pessoa.split("#")
    nome = dados_pessoa[0].split()[0][0]
    nota1 = float(dados_pessoa[1].replace(",", ".")) 
    nota2 = float(dados_pessoa[2].replace(",", ".")) 

    print (f"{nome:12s} {nota1+nota2:7.2f}")