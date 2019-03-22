'''
O tipo de figura geométrica (Q)uadrado, (R)etângulo ou (C)írculo.
Caso o usuário escolha quadrado, receba também com o tamanho do lado (float)
Caso o usuário escolha o retângulo, receba também a largura e a altura (float)
Caso o usuário escolha círculo, receba o tamanho do raio (float)
Formato de saída

Caso o usuário escolha quadrado ou retângulo, imprima a área e o perímetro
Caso o usuário escolha círculo, imprima a área e o comprimento do círculo (considere pi=3.14).
O valor de saída deve ser arredondado usando 2 casas decimais.


'''

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