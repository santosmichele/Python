'''
Descrição
José está prestes a inaugurar seu supermercado. Ele acredita que o cidadão brasileiro é capaz de pagar suas compras sozinho, 
sem precisar de um funcionário para conferir se o que ele está pagando corresponde aos produtos que ele está levando. 

Para isso ele vai precisar de um programa que irá ler o dia da semana, o preço do produto, a opção do produto ("prata" ou "ouro") e o nome. 

Se a compra estiver sendo realizada na segunda, terça ou quarta e a opção do produto for "ouro", o preço do produto ficará pela metade. 

Se a compra estiver sendo realizada na quinta ou sexta e o preço estiver entre R$ 10.00 e R$ 100.00, o preço será reduzido para um terço do valor original.

Se a compra estiver sendo realizada no sábado e a opção for prata, o preço do produto será o triplo.

Em qualquer outro caso, o preço será o dobro.

Formato de entrada

O dia da semana (string - "seg", "ter", "qua", "qui", "sex", "sab", "dom")
O preço do produto (float)
A opção do produto (string - "prata" ou "ouro")
O nome do produto
Formato de saída

Uma frase que indica o produto, o dia da semana da compra e o preço final do produto. Ex.:

"O preco do produto impressora no dia sab eh 250.0"
'''

diaCompra = input()
preco = float(input())
tipoProduto = input()
nomeProduto = input()

if ( (diaCompra == 'seg' or diaCompra == 'ter' or diaCompra == 'qua') and tipoProduto == 'ouro' ):
    preco = preco/2
elif ( (diaCompra == 'qui' or diaCompra == 'sex') and (preco >= 10 and preco <= 100) ):
    preco = preco / 3
elif ( (diaCompra == 'sab') and (tipoProduto == 'prata') ):
    preco = preco*3
else:
    preco = preco *2


print ("O preco do produto %s no dia %s eh %.2f" % (nomeProduto, diaCompra, preco) )
    
