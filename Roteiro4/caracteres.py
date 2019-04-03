###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

tamanhoPalavra = int(input())


while tamanhoPalavra > 0:
    palavra = input()
    novaPalavra = ''
    for i in range(tamanhoPalavra-1, -1, -1):
        novaPalavra += palavra[i]
    print (novaPalavra)
    tamanhoPalavra = int(input())