###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################
letra = input()
vogais = ['a', 'e', 'i','o','u']
if len(letra) > 1:
    print ("1 caractere, por favor!")
elif (letra.lower() in vogais):
    print ("Eh vogal")
else:
    print ("Nao eh vogal")