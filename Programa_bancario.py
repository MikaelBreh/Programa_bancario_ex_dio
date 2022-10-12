#programa banco
#devem haver tres opcoes: saque, deposito e extrato
#no extrato devem haver todas as operacoes
#sao permitidos apenas tres saques por dia no valor de 500 reais cada, tambem deve analisar se há saldo na conta
#no fim da listagem de extrato deve mostrar o saldo atual da conta

menu = """
[d] depositar 
[s] sacar
[e] extrato
[q] sair

"""
digitacao = 1

saldo = 0
saques = 0
limite_saques = 3

extrato_info = []
extrato_valor = []

print(menu)

while digitacao == 1:
    operacao = input(" \n Como podemos te ajudar hoje? ").lower()
    if operacao == 'd':
        deposito =  input("qual valor deseja depositar:")
        if int(deposito) >0:
            extrato_info.append('deposito +')
            extrato_valor.append(int(deposito))
            saldo += int(deposito)
        else:
            print("valor incorreto")

    elif operacao == 's':
        if saques < 3:
            saque = input("qual valor deseja sacar:")
            if int(saque) < 500 and int(saque) <= saldo and int(saque) > 0:
                extrato_info.append('saque -')
                extrato_valor.append(int(saque))
                saldo -= int(saque)
                saques += 1
            else:
                print("Você atingiu o limite por saque, ou está sem saldo na conta \n operação nao concluida!")
        else:
            print('limite de saques atingidos \n operação nao concluida')

    elif operacao == 'e':
        if len(extrato_valor) > 0:
            for a in range(len(extrato_valor)):
                print(extrato_info[a],  extrato_valor[a])
            print(f"""
            ========        EXTRATO      ========
            "valor total na conta: R$  {saldo:.2f}
            """)
        else:
            print('sem informacoes de movimentacao')
            print(f"""
            ========        EXTRATO      ========
            "valor total na conta: R$  {saldo:.2f}
                        """)

    elif operacao == 'q':
        print('ok, encerrando...')
        digitacao = 0

    else:
        print("selecione uma opcao valida!")
