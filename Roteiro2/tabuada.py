###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################



cont = 1    
inicio =  int(input())
while inicio <= 0 or inicio > 9:
    print ("Insira um número inicial entre 1 e 9")
    inicio =  int(input())

fim =  int(input())    
while fim <= 0 or fim > 9:    
    print ("Insira um número final entre 1 e 9")
    fim =  int(input())

    
if inicio > fim:
    print ("SEM RESPOSTA")
                  

while inicio <= fim:

    
    print("%d x %d = %d" % (inicio, cont, inicio * cont))
    cont += 1
    
    if cont == 10:
         cont = 1
         inicio += 1 
         print ()
         
    
