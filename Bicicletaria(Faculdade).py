def cadastrarPeca(codigo):
    print("Você selecionou a opção de cadastrar peça")

    codigo_peca = "{:03d}".format(codigo)
    print("Código da Peça:", codigo_peca)

    nome_peca = input("Por favor, entre com o nome da peça: ")
    fabricante_peca = input("Por favor, entre com o fabricante da peça: ")
    valor_peca = float(input("Por favor, entre com o valor (R$) da peça: "))

    peca = {
        "Código": codigo_peca,
        "Nome": nome_peca,
        "Fabricante": fabricante_peca,
        "Valor": valor_peca
    }

    return peca


def consultarPeca(pecas):
    print("Você selecionou a opção de consultar peças")

    while True:
        print("\nEscolha a opção desejada:")
        print("1 - Consultar Todas as Peças")
        print("2 - Consultar Peças por Código")
        print("3 - Consultar Peças por Fabricante")
        print("4 - Retornar")

        opcao = int(input(">>"))

        if opcao == 1:
            print("=====================================")
            for peca in pecas:
                print("Código: {:03d}".format(int(peca["Código"])))
                print("Nome: {}".format(peca["Nome"]))
                print("Fabricante: {}".format(peca["Fabricante"]))
                print("Valor: R$ {:.2f}".format(peca["Valor"]))
                print("-------------------------------------")

        elif opcao == 2:
            codigo_busca = int(input("Digite o código da peça: "))
            peca_encontrada = None
            for peca in pecas:
                if peca["Código"] == "{:03d}".format(codigo_busca):
                    peca_encontrada = peca
                    break

            if peca_encontrada:
                print("=====================================")
                print("Código: {:03d}".format(int(peca_encontrada["Código"])))
                print("Nome: {}".format(peca_encontrada["Nome"]))
                print("Fabricante: {}".format(peca_encontrada["Fabricante"]))
                print("Valor: R$ {:.2f}".format(peca_encontrada["Valor"]))
                print("-------------------------------------")
            else:
                print("Código de peça não encontrado.")

        elif opcao == 3:
            fabricante_busca = input("Digite o fabricante da peça: ")
            pecas_encontradas = []
            for peca in pecas:
                if peca["Fabricante"] == fabricante_busca:
                    pecas_encontradas.append(peca)

            if pecas_encontradas:
                print("=====================================")
                for peca in pecas_encontradas:
                    print("Código: {:03d}".format(int(peca["Código"])))
                    print("Nome: {}".format(peca["Nome"]))
                    print("Fabricante: {}".format(peca["Fabricante"]))
                    print("Valor: R$ {:.2f}".format(peca["Valor"]))
                    print("-------------------------------------")
            else:
                print("Peça com o fabricante especificado não encontrada.")

        elif opcao == 4:
            break


def removerPeca(pecas):
    print("Você selecionou a opção de remover peças")
    codigo_remover = int(input("Digite o código da peça a ser removida: "))
    peca_remover = None
    for peca in pecas:
        if peca["Código"] == "{:03d}".format(codigo_remover):
            peca_remover = peca
            break

    if peca_remover:
        pecas.remove(peca_remover)
        print("Peça removida com sucesso.")
    else:
        print("Código de peça não encontrado.")


def main():
    print("Bem-vindo ao Controle de Estoque da Bicicletaria do Thiago Henrique Dias de Oliveira")

    codigos_utilizados = []
    pecas = []

    while True:
        print("\nEscolha a opção desejada:")
        print("1 - Cadastrar Peças")
        print("2 - Consultar Peças")
        print("3 - Remover Peças")
        print("4 - Sair")

        opcao = int(input(">>"))

        if opcao == 1:
            codigo_peca = len(codigos_utilizados) + 1
            codigos_utilizados.append(codigo_peca)
            peca = cadastrarPeca(codigo_peca)
            pecas.append(peca)

        elif opcao == 2:
            consultarPeca(pecas)

        elif opcao == 3:
            removerPeca(pecas)

        elif opcao == 4:
            print("Saindo do programa...")
            break


if __name__ == "__main__":
    main()
