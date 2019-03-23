###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

homens = 0
mulheres = 0
salarioHomens = 0
salarioTotal = 0
maiorSalario = 0
sexoMaiorSalario = ''


for i in range(10):
    salario = float(input())
    sexo = (input())
    salarioTotal += salario
    if (salario > maiorSalario):
        maiorSalario = salario
        sexoMaiorSalario = sexo
        
    if (sexo == 'm'):
        homens += 1
        salarioHomens += salario
    elif (sexo == 'f'):
        mulheres += 1
print ("%i\n%i\n%.1f\n%s\n%.1f" %( homens ,mulheres, salarioTotal/(homens+mulheres)  , sexoMaiorSalario, salarioHomens/homens))