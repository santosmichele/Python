###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

totalDeVendas = 0
vendasAvista = 0
vendasNoCartao = 0
clienteMaisJovem = 999999
maiorCompra = 0
contatorAvista = 0
mediaCompras = 0


continuar = 'S'

while continuar == 'S':
    totalDeVendas += 1
    idade = int(input())
    if clienteMaisJovem > idade:
        clienteMaisJovem = idade

    valorCompra = float(input())
    if valorCompra > maiorCompra:
        maiorCompra = valorCompra

    formaPagamento = input()
    if formaPagamento == 'V':
        vendasAvista += valorCompra
        contatorAvista += 1
    else:
        vendasNoCartao += valorCompra
    continuar = input()
if contatorAvista > 0:
    mediaCompras = vendasAvista/contatorAvista

# Gambiarra feelings
# O teste automatico não considera quando 0.00 em alguns casos, esperando 0 como resposta
totalDeVendas = round(totalDeVendas, 2)
vendasAvista = round(vendasAvista, 2)
vendasNoCartao = round(vendasNoCartao, 2)
maiorCompra = round(maiorCompra, 2)
mediaCompras = round(mediaCompras, 2)

print (str(totalDeVendas) + '\n' + str(vendasAvista) + '\n' + str(vendasNoCartao) + '\n' + str(clienteMaisJovem) + '\n' + str(maiorCompra) + '\n' + str(mediaCompras))
#print ("%i\n%.2f\n%.2f\n%i\n%.2f\n%.2f" %(totalDeVendas, vendasAvista, vendasNoCartao, clienteMaisJovem, maiorCompra, mediaCompras) )