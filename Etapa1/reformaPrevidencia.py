###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

# casos de teste apresentam divergencia quando categoria SP e sexo F e em alguns casos a frase retorno termina em servidora e outras servidor
# em alguns casos a frase termina com ! e outras com . 

situacao = ""
categorias = ['PV', 'TR', 'SP', 'PR', 'PC']


categoriaTrabalhador = input()
categoriaTrabalhador = categoriaTrabalhador.upper()

if not(categoriaTrabalhador in categorias) :
    print ("Categoria de trabalhador invalida.")  
else:
    sexo = input()
    sexo = sexo.upper()

    idade = int(input())
    tempoContribuicao = int(input())

    if (categoriaTrabalhador == 'PV'):
        situacao += 'Trabalhador Privado '
        if ( not( (sexo == 'M' and idade >= 65) and tempoContribuicao >=20) or not(sexo == 'F' and idade >= 62 and tempoContribuicao >=20) ):
            situacao += 'NAO '

    elif (categoriaTrabalhador == 'TR'):
        situacao += 'Trabalhador Rural '
        if not(idade >= 60 and tempoContribuicao >=20):
            situacao += 'NAO '  

    elif (categoriaTrabalhador == 'SP'):
        situacao += 'Servidor publico '
        tempoServico = int(input())
        tempoCargo = int(input())
        if not(idade >= 60 and tempoContribuicao >=20) or not (tempoServico >=10 and tempoCargo >=5):
            situacao += 'NAO '
    elif (categoriaTrabalhador == 'PR'):
        situacao += 'Professor '
        if not( idade >= 60 and tempoContribuicao >=30 ):
            situacao += 'NAO '
    elif (categoriaTrabalhador == 'PC'):
        situacao += 'Policial '
        tempoExercito = int(input())
        if not( idade >= 55 and ( (sexo == 'M' and tempoContribuicao >= 30 and tempoExercito >=20) or (sexo =='F' and tempoContribuicao >=25 and tempoExercito >= 15))  ):
            situacao += 'NAO '
    situacao += 'pode se aposentar!'    
    print (situacao)