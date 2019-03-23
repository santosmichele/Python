###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################
notas = []
pesoNotas = []
mediaAritimetica = somaNotas =  mediaPonderada =  somaPesos = mediaHarmonica = 0


for x in range(0,3):
    notas.append(float(input()))
    somaNotas +=notas[x]
    
for x in range(0,3):
    pesoNotas.append(float(input()))
    somaPesos += pesoNotas[x]
    mediaPonderada += pesoNotas[x] * notas[x]

mediaAritimetica = somaNotas/len(notas)
mediaPonderada = mediaPonderada/somaPesos

for key, valor in enumerate(notas):
    mediaHarmonica += 1/notas[key]

mediaHarmonica = len(notas)/mediaHarmonica

print ("a: %.1f\np: %.1f\nh: %.1f" % (mediaAritimetica, mediaPonderada, mediaHarmonica))

