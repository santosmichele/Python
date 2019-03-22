'''
Descrição
Calcule o comprimento do arco de uma circunferência (a curva AB na figura) e a área do seu setor (delimitado pelo arco e hachurado de cinza na figura) 
usando os seguintes parâmetros:

O raio da circunferência (entre 1.0 e 50.0)
A medida do ângulo em graus (entre 0.0 e 359.0)
Use pi = 3.14
O valor de saída deve ser arredondado usando 2 casas decimais. Em Python 3, se sua variável de saída for v, use round(v, 2) 


Formato de entrada

O raio da circunferência (entre 1.0 e 50.0)

A medida do ângulo em graus (entre 0.0 e 359.0)

Formato de saída

A medida do comprimento do arco.

A área do setor.

'''

raio = float(input())
angulo = float(input())

pi = 3.14
comprimento = (angulo * pi * raio) / 180
areaSetor = (angulo/360)*pi*(raio**2)
print("%.2f\n%.2f" %(comprimento, areaSetor) )
