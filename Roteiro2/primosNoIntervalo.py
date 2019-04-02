###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################


inicioIntervalo = int(input())
fimIntervalo = int(input())

if (inicioIntervalo > fimIntervalo):
    menor = fimIntervalo
    fimIntervalo =inicioIntervalo
    inicioIntervalo = menor

for i in range(fimIntervalo, inicioIntervalo -1, -1):

    divisores = 0
    ehPrimo = True

    for n in range(1, i):
        if (i % n == 0):
            divisores += 1
        if (divisores > 1):
            ehPrimo = False
    if (ehPrimo):
        if (i != 1):
            print(i)