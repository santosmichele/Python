###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

totalBandejas = int(input())
contaCopos = 0
bandeja = [0 , 0]

#if (totalBandejas > 0 and totalBandejas <=100):
for i in range (totalBandejas):
    itensBandeja = input()
    itensBandeja = itensBandeja.split()
    bandeja[0] = int(itensBandeja[0])
    bandeja[1] = int(itensBandeja[1])
    if bandeja[0] > bandeja[1]:
        contaCopos += bandeja[1]
print (contaCopos)    
