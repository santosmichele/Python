'''Descrição
Seu Furustreco é um patrão justo. Ele decidiu pagar para cada funcionário além de cada hora extra, um adicional de 10% sobre cada hora extra.

Para ajudar seu Furustreco, você deve fazer um programa que recebe o salário base do empregado e quantas horas extras ele fez naquele mês. 
Você deve imprimir na saída padrão o salário final do empregado.

Dica: Você deve usar o salário base para calcular quanto custa uma hora extra do empregado. 
Considerando que a carga horária mensal de uma pessoa é de 44 horas.

O valor de saída deve ser arredondado usando 2 casas decimais.

Formato de entrada

Um valor real (float) que representa o salário do empregado e um valor inteiro que representa a quantidade de horas extras do empregado.

Considere o salário base um valor entre 1000.00 e 10000.00

A quantidade de horas extras por mês vai de 0 até 50.

Formato de saída

Um valor real (float) que representa o salário final do empregado.

O valor de saída deve ser arredondado usando 2 casas decimais.'''

salarioBase = float(input())
horasExtras = float(input())
valorHora = (salarioBase/44) 
valorHora = valorHora + (valorHora*(10/100))
salarioFinal = (valorHora*horasExtras) + salarioBase
print ("%.2f" %salarioFinal)