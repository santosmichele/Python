'''

Descrição
Em uma escola, um professor deve realizar três avaliações por semestre. Para o cálculo da nota final, ele pode usar três diferentes métodos de cálculo de médias:

Média aritmética ("a");

Média ponderada ("p"): nesse caso, o programa deve perguntar também os pesos de cada nota;

Média harmônica ("h"): pode ser definida pela quantidade de notas dividida pela soma do inverso de cada nota. Ex.: Se as notas forem 10, 7 e 5, a média harmônica 
será 3/(1/10+1/7+1/5)

Faça um programa que calcula as três médias para um conjunto de 3 notas. Na saída também deve ser identificado a qual média cada valor se refere.
Formato de entrada

Três notas entre 1 e 100 cada uma e os pesos (entre 1 e 10) para o cálculo da média ponderada.

A nota mínima é 1 para não dar erro de divisão por zero com a média harmônica.

Formato de saída

As médias aritmética, ponderada e harmônica.
'''
notas = []
pesoNotas = []
mediaAritimetica = somaNotas =  mediaPonderada =  somaPesos = mediaHarmonica = 0


for x in range(0,3):
    notas.append(float(input()))
    somaNotas +=notas[x]
    
for x in range(0,3):
    pesoNotas.append(float(input()))
    somaPesos += pesoNotas[x]
    mediaPonderada += pesoNotas[x] * notas[x]

mediaAritimetica = somaNotas/len(notas)
mediaPonderada = mediaPonderada/somaPesos

for key, valor in enumerate(notas):
    mediaHarmonica += 1/notas[key]

mediaHarmonica = len(notas)/mediaHarmonica

print ("a: %.1f\np: %.1f\nh: %.1f" % (mediaAritimetica, mediaPonderada, mediaHarmonica))

