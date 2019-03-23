###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################


escalaDeEntrada = input()
temperatura = float(input())
zeroKelvin = 273.15
msgErro = "Valor de temperatura abaixo do minimo"

if (escalaDeEntrada.upper() == 'C'):
    if (temperatura >= -273):
        converteParaF = (1.8*temperatura) +32
        converteParaK = temperatura + zeroKelvin
        print ("%.2f F\n%.2f K" % (converteParaF, converteParaK) ) 
    else:
        print (msgErro)
elif (escalaDeEntrada.upper() == 'F'):
    if (temperatura >= 459,67):
        converteParaC = (temperatura - 32) / 1.8
        converteParaK = converteParaC + zeroKelvin
        print ("%.2f C\n%.2f K" % (converteParaC, converteParaK) ) 
    else:
        print (msgErro)
elif (escalaDeEntrada.upper() == 'K'):
    if (temperatura >= 0):
        converteParaC = temperatura - zeroKelvin
        converteParaF = (1.8*(temperatura - zeroKelvin) +32)
        print ("%.2f C\n%.2f F" % (converteParaC, converteParaF) ) 
    else:
        print (msgErro)




