###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

contador = 0
somaNotas = 0
menorNota = 1000
matricula = int(input())
matriculaMenorNota = 0
while not(matricula == 999):
    contador += 1
    nota = float(input())
    if nota < menorNota:
        menorNota = nota
        matriculaMenorNota = matricula
    somaNotas += nota
    matricula = int(input())
print ("%d\n%.2f" %(matriculaMenorNota, (somaNotas/contador) ) )