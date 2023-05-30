print("Bem vindo a loja do Thiago Henrique Dias de Oliveira")

valorProduto = float(input("Entre com o valor do produto: "))  # Solicita ao usuário o valor do produto
qnteProduto = int(input("Entre com valor do quantidade: "))  # Solicita ao usuário a quantidade de produtos
valorTotal = valorProduto * qnteProduto  # Calcula o valor total da compra

if 0 <= qnteProduto <= 9:  
    # Se a quantidade de produtos for menor ou igual a 9, não terá desconto!
    porcentagem = 0
elif 10 <= qnteProduto <= 99:  
    # Se a quantidade de produtos for maior ou igual a 10 e menor ou igual a 99, terá 5% de desconto!
    porcentagem = 5
elif 100 <= qnteProduto <= 999:
    # Se a quantidade de produtos for maior ou igual a 100 e menor ou igual a 999, terá 10% de desconto!
    porcentagem = 10
else:
    # Se a quantidade de produtos for maior que 999, terá 15% de desconto!
    porcentagem = 15

desconto = valorTotal * porcentagem / 100  # Calcula o valor do desconto em reais
valorDesconto = valorTotal - desconto  # Calcula o valor total com desconto

print("O valor sem desconto foi: R${:.2f}".format(valorTotal))  # Exibe o valor total sem desconto
print("O valor com desconto foi: R${:.2f}  (desconto {}%)".format(valorDesconto, porcentagem))  # Exibe o valor total com desconto e a porcentagem aplicada
  