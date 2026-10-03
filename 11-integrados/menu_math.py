import datetime

opcao = 0

while opcao != 6:
    print (
    '''
    1 - Calcular a área de um triangulo
    2 - Calcular a idade de uma pessoa
    3 - Calcular a multa de atraso de fatura de cartao de credito
    4 - Indicar se um número é decrescente (Allef)
    5 - Indicar se um número é decrescente (Angelo)
    6 - Sair
    ''')

    opcao = int(input ("Escolha uma opcao: "))
    if opcao == 1:
        B = float(input("Digite a base do triangulo: "))
        H = float(input("Digite a altura do triangulo: "))
        A = (B * H) / 2

        print("A área do triangulo é:", A)
    if opcao == 2:
        Ano_nascimento = int(input("Digite o ano de nascimento: "))
        Ano_atual = datetime.datetime.now().year
        Idade = Ano_atual - Ano_nascimento

        print("A idade da pessoa é:", Idade)
    if opcao == 3:
        Valor_fatura = float(input("Digite o valor da fatura: "))
        Valor_multa = Valor_fatura * 0.02

        print("O valor da multa de atraso é:", Valor_multa)
    if opcao == 4:
        numero = input("Digite um número inteiro: ")

        decrescente = True 
        for pos in range(len(numero) - 1):
            if numero[pos] < numero[pos+1]:
                decrescente = False
                break
        if decrescente == True:
            print (numero, "é decrescente.")
        else:
            print (numero, "não é decrescente.")
    if opcao == 5:
        print ("Você escolheu: verificar se um número é decrescente")
        numero = int(input("Digite um número para saber se é decrescente: "))
        decrescente = True
        while numero > 10:
            digito_atual = numero % 10
            digito_anterior = (numero // 10) % 10 
            if digito_anterior < digito_atual:
                decrescente = False
                break
            numero = numero // 10    
        
        if decrescente == True:
            print (numero, "é decrescente.")
        else:
            print (numero, "não é decrescente.")
