saldo = 0
lista_depositos = []
lista_saques = []
qtde_saques = 0
LIMITE_DIARIO_SAQUES = 3
LIMITE_VALOR_SAQUES = 500
while True:
    OPERACAO = int(input("""
    *** SISTEMA BANCÁRIO ***
        
    [1] DEPOSITAR
    [2] SACAR
    [3] EXIBIR EXTRATO
    [0] SAIR
        
    SELECIONE UMA OPERAÇÃO => """))
    if OPERACAO == 1:
        deposito = float(input("\nDigite o valor á ser depositado: R$ "))
        if deposito <= 0:
            print("\n*** VALOR INVÁLIDO! REINICIANDO SISTEMA! ***\n")
        else:
            saldo += deposito
            lista_depositos.append(deposito)
            print("\n*** DEPÓSITO EFETUADO COM SUCESSO! REINICIANDO SISTEMA! ***")
    elif OPERACAO == 2:
        if qtde_saques == LIMITE_DIARIO_SAQUES:
            print("\n*** OPERAÇÃO INVÁLIDA: LIMITE DE SAQUES DIÁRIOS (3) EXCEDIDO! REINICIANDO SISTEMA! ***")
        else:
            saque = float(input("\nDigite o valor á ser sacado: R$ "))
            if saque > LIMITE_VALOR_SAQUES:
                print("\n*** OPERAÇÃO INVÁLIDA: VALOR LIMITE DE SAQUE (R$ 500.00) EXCEDIDO! REINICIANDO SISTEMA! ***")
            elif saque > saldo:
                print("\n*** OPERAÇÃO INVÁLIDA: SALDO INSUFICIENTE PARA SAQUE! REINICIANDO SISTEMA! ***")
            elif saque <= 0:
                print("\n*** VALOR INVÁLIDO! REINICIANDO SISTEMA! ***\n")
            else:
                saldo -= saque
                lista_saques.append(saque)
                qtde_saques += 1
                print("\n*** SAQUE EFETUADO COM SUCESSO! REINICIANDO SISTEMA! ***")
    elif OPERACAO == 3:
        print("\n*** EXIBINDO EXTRATO ***\n")
        for indice in range(len(lista_depositos)):
            print(f"{indice+1}º DEPÓSITO: R$ {lista_depositos[indice]:.2f}")
        for indice in range(len(lista_saques)):
            print(f"{indice+1}º SAQUE: R$ {lista_saques[indice]:.2f}")
        print(f"\n*** SALDO ATUAL DA CONTA: R${saldo:.2f}! REINICIANDO SISTEMA! ***")
    elif OPERACAO == 0:
        print("\n*** ENCERRANDO SISTEMA! ***\n")
        break
    else:
        print("*** SELEÇÃO INVÁLIDA! REINICIANDO SISTEMA! ***")
