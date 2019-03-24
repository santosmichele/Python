###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

n1 = int(input())
i = 1
t = 0
multiploUm = multiploDois = multiploTres = 0
while t < n1:
    t = i*(i+1)*(i+2)    
    multiploUm = i
    multiploDois = i+1
    multiploTres = i+2
    i += 1

if not(t == n1) or n1 == 0:
    print ('Falso')    
else: 
    print ('%i * %i * %i = %i\nVerdadeiro' %(multiploUm, multiploDois, multiploTres, n1))
	