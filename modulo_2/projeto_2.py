saldo = 0
qtde_saques = 0
qtde_contas = 0
extrato = ""
usuarios = []
contas = []

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("\n*** VALOR INVÁLIDO! REINICIANDO SISTEMA! ***")
        return saldo, extrato
    else:
        saldo += valor
        extrato += f"DEPÓSITO: R${valor:.2f}\n"
        print("\n*** DEPÓSITO EFETUADO COM SUCESSO! REINICIANDO SISTEMA! ***")
        return saldo, extrato

def sacar(*, saldo, valor, extrato, LIMITE_VALOR_SAQUES, LIMITE_DIARIO_SAQUES, qtde_saques):
    if qtde_saques == LIMITE_DIARIO_SAQUES:
        print("\n*** OPERAÇÃO INVÁLIDA: LIMITE DE SAQUES DIÁRIOS (3) EXCEDIDO! REINICIANDO SISTEMA! ***")
        return saldo, extrato, qtde_saques
    else:
        if valor > LIMITE_VALOR_SAQUES:
            print("\n*** OPERAÇÃO INVÁLIDA: VALOR LIMITE DE SAQUE (R$ 500.00) EXCEDIDO! REINICIANDO SISTEMA! ***")
            return saldo, extrato, qtde_saques
        elif valor > saldo:
            print("\n*** OPERAÇÃO INVÁLIDA: SALDO INSUFICIENTE PARA SAQUE! REINICIANDO SISTEMA! ***")
            return saldo, extrato, qtde_saques
        elif valor <= 0:
            print("\n*** OPERAÇÃO INVÁLIDA: VALOR MENOR DO QUE ZERO! REINICIANDO SISTEMA! ***")
            return saldo, extrato, qtde_saques
        else:
            saldo -= valor
            extrato += f"SAQUE: R${valor:.2f}\n"
            qtde_saques += 1
            print("\n*** SAQUE EFETUADO COM SUCESSO! REINICIANDO SISTEMA! ***")
            return saldo, extrato, qtde_saques

def exibir_extrato(saldo, /, *, extrato):
    print(f"\n{extrato}")
    print(f"*** SALDO ATUAL DA CONTA: R${saldo:.2f}! REINICIANDO SISTEMA! ***")

def criar_usuario():
    nome = input("NOME: ")
    data_nasc = input("DATA DE NASCIMENTO: ")
    cpf = int(input("CPF: "))
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            cpf = False
    if cpf is False:
        print("\n*** OPERAÇÃO INVÁLIDA: CPF JÁ CADASTRADO! REINICIANDO SISTEMA! ***")
        return False
    else:
        logradouro = input("ENDEREÇO (LOGRADOURO): ")
        numero = input("ENDEREÇO (NÚMERO): ")
        bairro = input("ENDEREÇO (BAIRRO): ")
        cidade = input("ENDEREÇO (CIDADE): ")
        sigla_estado = input("ENDEREÇO (SIGLA DO ESTADO): ")
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"
        print("\n*** CRIAÇÃO DE USUÁRIO EFETUADA COM SUCESSO! REINICIANDO SISTEMA! ***")
        return {"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco}

def criar_conta(qtde_contas):
    contador = 0
    cpf = int(input("CPF DO USUÁRIO DA CONTA: "))
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            contador += 1
            break
    if contador == 1:
        print("\n*** CRIAÇÃO DE CONTA BANCÁRIA EFETUADA COM SUCESSO! REINICIANDO SISTEMA! ***")
        qtde_contas += 1
        return {"numero_agencia": "0001", "numero_conta": qtde_contas, "cpf_usuario": cpf}
    else:
        print("\n*** OPERAÇÃO INVÁLIDA: CPF NÃO ENCONTRADO! REINICIANDO SISTEMA! ***")
        return False

while True:
    OPERACAO = int(input("""
    *** SISTEMA BANCÁRIO ***
        
    [1] DEPOSITAR
    [2] SACAR
    [3] EXIBIR EXTRATO
    [4] CRIAR USUÁRIO
    [5] CRIAR CONTA BANCÁRIA
    [0] SAIR
        
    SELECIONE UMA OPERAÇÃO => """))
    if OPERACAO == 1:
        print("\n*** DEPOSITAR ***")
        valor = float(input("\nDigite o valor á ser depositado: R$ "))
        deposito = depositar(saldo, valor, extrato)
        saldo = deposito[0]
        extrato = deposito[1]
    elif OPERACAO == 2:
        print("\n*** SACAR ***")
        valor = float(input("\nDigite o valor á ser sacado: R$ "))
        saque = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            LIMITE_VALOR_SAQUES=500,
            LIMITE_DIARIO_SAQUES=3,
            qtde_saques=qtde_saques
        )
        saldo = saque[0]
        extrato = saque[1]
        qtde_saques = saque[2]
    elif OPERACAO == 3:
        print("\n*** EXIBIR EXTRATO ***")
        exibir_extrato(saldo, extrato=extrato)
    elif OPERACAO == 4:
        print("\n*** CRIAR USUÁRIO ***\n")
        usuario = criar_usuario()
        if usuario is not False:
            usuarios.append(usuario)
    elif OPERACAO == 5:
        print("\n*** CRIAR CONTA BANCÁRIA ***\n")
        conta = criar_conta(qtde_contas)
        if conta is not False:
            contas.append(conta)
            qtde_contas += 1
    elif OPERACAO == 0:
        print("\n*** ENCERRANDO SISTEMA! ***\n")
        break
    else:
        print("*** SELEÇÃO INVÁLIDA! REINICIANDO SISTEMA! ***\n")
