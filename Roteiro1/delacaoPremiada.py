###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################


delacao = 'Delação rejeitada.'

crimeDelatador = input()

if (crimeDelatador not in ['roubo', 'tráfico', 'homicídio']):
    print ("Crime inválido.")
else:
    if not(crimeDelatador == 'homicídio'):
        valorCrimeDelatador = int(input())

    crimeDelatado = input()

    if (crimeDelatado not in ['roubo', 'tráfico', 'homicídio']):
        print ("Crime inválido.")

    else:
        if (crimeDelatado == 'roubo' or crimeDelatado == 'tráfico' ):
            valorCrimeDelatado = int(input())

        #Se o crime do delator for de roubo ou tráfico e o crime delatado for de homicídio, ele tem direito à delação diretamente
        #No caso do delator ter cometido um homicídio e quiser delatar um homicídio, a delação será concedida
        if ( (crimeDelatado == 'homicídio') ):
            delacao = 'Delação concedida.'

        #Se o crime do delator for de roubo e o crime delatado for também de roubo, ele só tem direito à delação se o valor do roubo 
        # delatado for mais de 5 vezes maior que o do roubo do delator
        elif ( (crimeDelatador == 'roubo' and crimeDelatado == 'roubo') and valorCrimeDelatador*5 < (valorCrimeDelatado)):
            delacao = 'Delação concedida.'

        #Se o crime do delator for de roubo e o crime delatado for de tráfico, ele só tem direito à delação se o valor da droga 
        # traficada for mais de 3 vezes maior que o do roubo do delator
        elif ( (crimeDelatador == 'roubo' and crimeDelatado == 'tráfico') and (valorCrimeDelatado > 3*valorCrimeDelatador) ):
            delacao = 'Delação concedida.'
            

        #Se o crime do delator for de tráfico e o crime delatado for de tráfico, ele só tem direito à delação se o valor da droga traficada for 
        # mais de 5 vezes maior que o do tráfico do delator
        elif ( (crimeDelatador == 'tráfico' and crimeDelatado == 'tráfico') and valorCrimeDelatado > 5*(valorCrimeDelatador)):
            delacao = 'Delação concedida.'


        print (delacao)