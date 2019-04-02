###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

contador  = 0
somaPontos = 0
menor = 10000
menorPontuador = ''
maiorPontuador = ''
maior = -1
nomeJogador = input()
if nomeJogador.upper() == 'SAIR':
    print("Nenhum jogador foi registrado.")
else:
    while nomeJogador.upper() != 'SAIR':
        contador += 1
        pontos = int(input())
        somaPontos +=pontos
        if pontos <= menor:
            menor = pontos
            menorPontuador = nomeJogador
        if pontos >= maior:
            maior = pontos
            maiorPontuador = nomeJogador
        nomeJogador = input()



    print ("%s\n%s\n%.2f" %(menorPontuador, maiorPontuador, (somaPontos/contador) ) )