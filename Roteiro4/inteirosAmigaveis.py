###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

caracteresPermitidos = '0123456789oOl'
inteiro = input()

while inteiro != 'FIM':
    erro = False
    for i in range(len(inteiro)):
        if inteiro[i] in caracteresPermitidos:
            pass
        else:
            erro = True
            break
        
    if (erro):
        print ("ERRO")
    else:
        
        inteiro = inteiro.replace('o', '0')
        inteiro = inteiro.replace('O', '0')
        inteiro = inteiro.replace('l', '1')
        print (int(inteiro))
       
    inteiro = input()

