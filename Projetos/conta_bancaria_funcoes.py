def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é invalido.")
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número):")
    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero da casa, bairro, cidade, estado): ")
    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def conta_corrente(agencia, numero_da_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente numeros)")
    print("\n Conta criada com sucesso!")
    return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuarios": usuarios}

def main():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta corrente
    [0] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 5
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:

        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            extrato(saldo, extrato = extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = conta_corrente(AGENCIA, numero_da_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()