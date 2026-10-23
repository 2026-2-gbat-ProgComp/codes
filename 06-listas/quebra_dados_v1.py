dados = """Galileu Batista,5.0,2.5;Maria Candida Xavier,8,5;Damiao Pedro,7.5,8"""

# Mostre o primeiro nome e a soma das notas de cada aluno.

dados2 = dados.split()
# print (dados2)
# ['Galileu', 'Batista,5.0,2.5;Maria', 'Candida', 'Xavier,8,5;Damiao', 'Pedro,7.5,8']

pessoas = dados.split(";")
# print (pessoas)
# ['Galileu Batista,5.0,2.5', 'Maria Candida Xavier,8,5', 'Damiao Pedro,7.5,8']

for pessoa in pessoas:
    # print (pessoa)
    dados_pessoa = pessoa.split(",")
    # ['Galileu Batista', '5.0', '2.5']
    nota_pessoa = float(dados_pessoa[1]) + float(dados_pessoa[2])
    # print (dados_pessoa[0], nota_pessoa)
    nome_pessoa = dados_pessoa[0].split(" ")[0]
    print (nome_pessoa, nota_pessoa)