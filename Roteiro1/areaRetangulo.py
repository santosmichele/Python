'''
Descrição
Faça um programa que calcule a área de um retângulo a partir dos tamanhos de seu lado maior e de seu lado menor.

Formato de entrada

Os valores em sequência dos lados do retângulo.

Os valores estão necessariamente entre 1 e 1000.

Formato de saída

O valor da área do retângulo.
'''

base = int(input())
altura = int(input())
if (base >=0 and base <= 1000 and altura >= 0 and altura <=1000):
    print (base*altura)