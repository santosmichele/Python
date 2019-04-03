###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

numeroEntradas = int(input())
acimaMedia = 0
abaixoMedia = 0
notas = []
for i in range(numeroEntradas):
    notas.append(float(input()))
media = (sum(notas)/numeroEntradas)

for n in range (numeroEntradas):
    
    if (media + media*0.1) <= notas[n]:
        acimaMedia += 1
    if (media - media*0.1) >= notas[n]:
        abaixoMedia += 1
print ("%.2f\n%d\n%d"   %(media, acimaMedia, abaixoMedia))