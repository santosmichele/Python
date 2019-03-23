###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

 
listaTimes = ['GSW', 'HOU', 'CLE', 'BOS']
time = input()


if not(time in listaTimes):
    print ("Nenhum time de interesse jogando.")
else:
    pontosTotais = 0
    nomeJogador = input()

    arremessostentadosDoisPontos = float(input())
    
    
    arremessosConvertidosDoisPontos = float(input())
    pontosTotais += (arremessosConvertidosDoisPontos*2)

    percentualDeAcertoDoisPontos = (100*arremessosConvertidosDoisPontos) / arremessostentadosDoisPontos

    arremessosTentatosTresPontos = float(input())
    

    arremessosConvertidosTresPontos = float(input())
    pontosTotais += (arremessosConvertidosTresPontos*3)

    percentualDeAcertoTresPontos = (100*arremessosConvertidosTresPontos) / arremessosTentatosTresPontos
    
    # Se a estatística de pontos totais for maior que 30
    #OU se o percentual de acerto de arremessos de 2 pontos for maior que 50% e a quantidade de arremessos tentados for maior que 10
    #OU se o percentual de acerto de arremessos de 3 pontos for maior que 40% e a quantidade de arremessos tentados for maior que 7
    if (pontosTotais > 30 or 
        + (percentualDeAcertoDoisPontos > 50 and arremessostentadosDoisPontos > 10 ) or 
        + (percentualDeAcertoTresPontos > 40 and arremessosTentatosTresPontos) ):
        print ("O time %s estah jogando, e %s estah indo bem." %(time, nomeJogador))
    else:
        print("O time %s estah jogando, mas %s nao estah indo bem." %(time, nomeJogador))
