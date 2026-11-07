lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

# Imprimir na tela os dados obedecendo o seguinte layout:
# 'O estado NOME_ESTADO (SIGLA) possui (QUANTIDADE) habitantes'
# Sendo que em ordem decrescente da quantidade de habitantes

# E no final imprimir a seguinte informação:
# 'O Nordeste possui um total de (QUANTIDADE TOTAL) habitantes'

lst_populacao2 = sorted(lst_populacao, reverse=True)
for pop in lst_populacao2:
    pos = lst_populacao.index(pop)
    print (f'O estado {lst_uf[pos]} ({lst_siglas[pos]}) possui ({lst_populacao[pos]}) habitantes')
print ("*"*60)

lst_populacao2 = sorted(enumerate(lst_populacao), 
                        key=lambda x:x[1],
                        reverse=True)
for pos, _ in lst_populacao2:
    print (f'O estado {lst_uf[pos]} ({lst_siglas[pos]}) possui ({lst_populacao[pos]}) habitantes')
