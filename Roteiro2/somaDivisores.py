###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################


# aqui eh uma tupla pois consome menos que uma lista e nao pretendemos mudar as entradas no futuro
entradas = ( int(input()) , int(input()) , int(input()) , int(input()) , int(input()) )
somaDivisores = 0
resultado = 0


for posicao in range (len(entradas)):
    comparador = 0
    for divisor in range(1,(entradas[posicao]+1)):
        if entradas[posicao]%divisor == 0:
            comparador += divisor
    if comparador > somaDivisores:
        somaDivisores = comparador
        resultado = entradas[posicao]
    
print (resultado)