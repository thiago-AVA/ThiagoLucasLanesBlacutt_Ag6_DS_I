# Desconto progressivo

#Este programa calcula o preço final de um produto com base no desconto progressivo aplicado de acordo com a quantidade comprada.

## entrada de dados ##

print("bem-vindo ao programa de desconto progressivo!")
preco_da_unidade = float(input("Digite o preço do produto: "))
quantidade_de_produtos = int(input("Digite a quantidade de produtos comprados: "))

## processamento ##

#valor total da compra, pegando o valor do produto e a quantidade dele, multiplicando ele.

valor_total = preco_da_unidade * quantidade_de_produtos

#descontos e saida, separação de descontos e saída de mensagem com o valor ja com o desconto aplicado a compra.

if valor_total >= 300.00:
    desconto_15 = print("parabéns, vc recebeu um desconto de 15%, sua compra ficou por",valor_total * 0.85)
elif valor_total >= 200.00:
    desconto_10 = print("parabéns, vc recebeu um desconto de 10%, sua compra ficou por",valor_total * 0.90)
else:
    desconto_5 = print("parabéns, vc recebeu um desconto de 5%, sua compra ficou por",valor_total * 0.95)

