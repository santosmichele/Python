###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

contador = 0
continuar = ''
maiorVelocidade = 0
maiorAno = 0
velocidadeMedia = 0


while True:
    continuar = input()
    if (continuar.upper() == 'N'):
        break
    ano = int(input())
    if (maiorAno < ano):
        maiorAno = ano

    velocidade = float(input())
    if (maiorVelocidade < velocidade):
        maiorVelocidade = velocidade

    contador += 1
    velocidadeMedia += velocidade
    
if contador > 0:
    velocidadeMedia /= contador
    print ('%.2f\n%i\n%.2f' %(maiorVelocidade, maiorAno, velocidadeMedia) )
else:
    print ("zero")