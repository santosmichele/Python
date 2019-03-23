###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################
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
    
