###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

notas = []
pesoNotas = []
somaNotas  =  somaPesos = mediaFinal = 0
status = ""

mediaEscolhida = input()
if not(mediaEscolhida in ['a', 'p', 'h']):
    print ("Escolha um tipo de media valida.")
    
else:
    for x in range(0,3):
        notas.append(int(input()))
        somaNotas +=notas[x]
    if (mediaEscolhida == 'a'):
        mediaFinal = somaNotas/len(notas)

    elif (mediaEscolhida == 'p'):
        for x in range(0,3):
            pesoNotas.append(float(input()))
            somaPesos += pesoNotas[x]
            mediaFinal += pesoNotas[x] * notas[x]
        mediaFinal = mediaFinal/somaPesos
    
    elif (mediaEscolhida == 'h'):
        for key, valor in enumerate(notas):
            mediaFinal += 1/notas[key]
        mediaFinal = len(notas)/mediaFinal
        

    if ( mediaFinal >= 70 and mediaFinal <= 100):
        status = "Aprovado"
    elif ( mediaFinal >= 40 and mediaFinal < 70):
        status = "Final"
    elif ( mediaFinal >= 0 and mediaFinal < 40):
        status = "Reprovado"

    if (mediaFinal < 0 or mediaFinal > 100):
        print ("Media invalida")
    else:
        print ("%.2f\n%s" %(mediaFinal, status))
