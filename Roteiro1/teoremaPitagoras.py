'''Descrição
Faça um programa que calcule o valor da hipotenusa de acordo com o teorema de pitágoras. Você não precisa se 
preocupar com casos em que os catetos fornecidos não podem formar um triângulo.

Pesquise como fazer a operação de raiz quadrada.

O valor de saída deve ser arredondado usando 2 casas decimais.

Formato de entrada

Os valores (reais) dos dois catetos.

Formato de saída

O valor da hipotenusa.'''

catetoUm = float(input())
catetoDois = float(input())
hipotenusa = ((catetoUm**2) + (catetoDois**2))**(1/2)
print ("%.2f" %hipotenusa)