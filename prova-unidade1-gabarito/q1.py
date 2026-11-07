saldo_real = 0
limite_especial = 0

opcao = 'X'
while opcao != 'Q':
    opcao = input ("""
            Operações disponíveis:
                D: realização de um depósito; 
                R: realização de uma retirada (saque); 
                E: envio de Pix; 
                P: pagamento de boleto;  
                S: consulta de saldo; 
                C: concessão de cheque especial; 
                Q: Sai do programa;
           
           Escolha: 
           """).upper()
    
    if opcao == 'D':
        valor = float(input("Valor: "))
        if valor >= 0:
            saldo_real += valor
        else:
            print ("Valor inválido.")
    elif opcao == 'C':
        if limite_especial == 0:
            valor = float(input("Valor do cheque especial: "))
            if valor > 0:
                limite_especial = valor
            else:
                print ("Valor inválido.")
        else:
            print ("Cheque especial ja concedido!")
    elif opcao in ['R', 'E', 'P']:
        valor = float(input("Valor: "))
        if valor > 0:
            if valor <= (saldo_real+limite_especial):
                saldo_real -= valor
            else:
                print ("Saldo insuficiente!")
        else:
            print ("Valor inválido.")
    elif opcao == 'S':
        print (f"Saldo real: R${saldo_real:6.2f} Limite {limite_especial:6.2f} "+
               f"Disponível {saldo_real+limite_especial:6.2f}")
    elif opcao != 'Q':
        print ("Opção inválida ...")