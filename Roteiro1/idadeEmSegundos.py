'''
Descrição
Escreva um programa que leia a idade de uma pessoa e informe quantos segundos ela viveu.

Formato de entrada

A idade de uma pessoa em anos.

Formato de saída

A mesma idade conertida para segundos.


60 segundos= 1 minuto
60 minutos = 3600s
24 horas= 86400
30 dias = 1 mes
12 meses = 32636000
'''

idadeEmAnos = int(input())
print (idadeEmAnos*31536000)