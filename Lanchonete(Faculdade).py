print("Bem vindo à lanchonete do Thiago Henrique Dias de Oliveira")
print("*************** Cardápio ***************") 
print("| Código |        Descrição        | Valor |")
print("|   100  |     Cachorro Quente     |  9,00 |")
print("|   101  |  Cachorro Quente Duplo  | 11,00 |")
print("|   102  |           X-Egg         | 12,00 |")
print("|   103  |         X-Salada        | 12,00 |")
print("|   104  |          X-Bacon        | 14,00 |")
print("|   105  |          X-Tudo         | 17,00 |")
print("|   200  |    Refrigerante Lata    |  5,00 |")
print("|   201  |       Chá gelado        |  4,00 |")

valorTotal = 0  # Inicializa a variável "valorTotal" como zero para armazenar o valor total dos pedidos

while True:
    codigo = int(input("Entre com o código desejado: "))

    valor = 0  # Inicializa a variável "valor" como zero para armazenar o valor do pedido
    pedido = ""  # Inicializa a variável "pedido" como uma string vazia para armazenar o nome do produto do pedido

    if codigo == 100:
        pedido = "Cachorro Quente"
        valor = 9.00
    elif codigo == 101:
        pedido = "Cachorro Quente Duplo"
        valor = 11.00
    elif codigo == 102:
        pedido = "X-Egg"
        valor = 12.00
    elif codigo == 103:
        pedido = "X-Salada"
        valor = 12.00
    elif codigo == 104:
        pedido = "X-Bacon"
        valor = 14.00
    elif codigo == 105:
        pedido = "X-Tudo"
        valor = 17.00
    elif codigo == 200:
        pedido = "Refrigerante Lata"
        valor = 5.00
    elif codigo == 201:
        pedido = "Chá gelado"
        valor = 4.00
    else:
        print("Opção inválida")  # Imprime uma mensagem de opção inválida se o código digitado não estiver na lista
        continue  # Volta ao início do loop

    valorTotal += valor  # Adiciona o valor do pedido ao valor total
    print("Você pediu um {} no valor de R$ {:.2f}".format(pedido, valor).replace('.', ','))

    escolha = int(input("Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não \n>>"))
    if escolha == 0:
        break

print("O total a ser pago é: R$ {:.2f}".format(valorTotal).replace(',', '.'))