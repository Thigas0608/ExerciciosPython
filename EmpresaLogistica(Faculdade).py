def dimensoesObjeto():
    while True:
        try:
            # Solicita as dimensões do objeto
            comprimento = int(input("Digite o comprimento do objeto (em cm): "))
            largura = int(input("Digite a largura do objeto (em cm): "))
            altura = int(input("Digite a altura do objeto (em cm): "))

            # Calcula o volume do objeto
            volumeObjeto = comprimento * largura * altura

            # Exibe o volume do objeto
            print("O volume do objeto é (em cm³): {:.1f}".format(volumeObjeto))

            if volumeObjeto > 100000:
                # Verifica se o volume excede o limite máximo
                print("Não aceitamos objetos com dimensões tão grandes \nEntre com as dimensões desejados novamente")
            else:
                if volumeObjeto < 1000:
                    Valor = 10
                elif 1000 <= volumeObjeto < 10000:
                    Valor = 20
                elif 10000 <= volumeObjeto < 30000:
                    Valor = 30
                elif 30000 <= volumeObjeto < 100000:
                    Valor = 50
                else:
                    print("O volume do objeto é maior que 100000. \nPor favor, digite um valor menor que 100000.")
                    continue

                # Se o volume estiver dentro do limite, retorna o valor
                return Valor

        except ValueError:
            # Tratamento de exceção para entrada inválida
            print("Você digitou alguma dimensão do objeto com valor não numérico \nPor favor entre com as dimensões desejadas novamente")


def pesoObjeto():
    while True:
        try:
            # Solicita o peso do objeto
            pesoObjeto = int(input("Digite o peso do objeto (em kg):"))

            if pesoObjeto > 9999:
                # Verifica se o peso excede o limite máximo
                print("Não aceitamos objetos tão pesados \nEntre com o peso desejado novamente")
            else:
                # Se o peso estiver dentro do limite, retorna o multiplicador
                if pesoObjeto <= 0.1:
                    Multiplicador = 1
                elif 0.1 <= pesoObjeto < 1:
                    Multiplicador = 1.5
                elif 1 <= pesoObjeto < 10:
                    Multiplicador = 2
                elif 10 <= pesoObjeto <= 30:
                    Multiplicador = 3

                return Multiplicador

        except ValueError:
            # Tratamento de exceção para entrada inválida
            print("Você digitou peso do objeto com um valor não numérico \nPor favor entre com o peso desejado novamente")


def rotaObjeto():
    while True:
        # Exibe o menu de rotas
        print("Selecione a rota:")
        print(" BR - De Brasília para Rio de Janeiro")
        print(" BS - De Brasília para São Paulo")
        print(" RB - De Rio de Janeiro para Brasília")
        print(" RS - De Rio de Janeiro para São Paulo")
        print(" SR - De São Paulo para Rio de Janeiro")
        print(" SB - De São Paulo para Brasília")

        rota = str(input(">> "))

        if rota == "RS" or rota == "SR":
            MultiplicadorRota = 1
            break
        elif rota == "BS" or rota == "SB":
            MultiplicadorRota = 1.2
            break
        elif rota == "BR" or rota == "RB":
            MultiplicadorRota = 1.5
            break
        else:
            print("Você digitou uma rota que não existe \nPor favor entre com a rota desejada novamente")

    return MultiplicadorRota


print("Bem vindo a Companhia de Logística Thiago Henrique Dias de Oliveira.")

Valor = dimensoesObjeto()
MultiplicadorPeso = pesoObjeto()
MultiplicadorRota = rotaObjeto()

TotalPagar = Valor * MultiplicadorPeso * MultiplicadorRota

print("Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota: {})".format(TotalPagar, Valor, MultiplicadorPeso, MultiplicadorRota))
