###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

tipoFigura = input()
tipoFigura = tipoFigura.upper()

if  not( tipoFigura in ['Q' , 'R' , 'C'] ):
    print ("Nenhuma figura selecionada")
elif (tipoFigura == 'Q'):
    lado = float(input())
    print ("%.2f\n%.2f" % ((lado**2),(lado*4)))
elif (tipoFigura == 'R'):
    base = float(input())
    altura = float(input())
    print ("%.2f\n%.2f" % ((base*altura),(base*2 + altura*2)))
elif (tipoFigura == 'C'): 
    raio = float(input())
    print ("%.2f\n%.2f" % ( ( 3.14*(raio**2) ) , ( (2*3.14) * raio) ) )