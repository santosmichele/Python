'''
Descrição
Escreva um programa que calcule a quantidade máxima de dados a ser transmitida por um usuário levando em consideração a taxa de transmissão maxima de vídeo, 
áudio e dados e a capacidade do canal contratado:

QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade

O valor de saída deve ser arredondado usando 2 casas decimais. Em Python 3, se sua variável de saída for QDmax, use round(QDmax, 2)

Formato de entrada

Os valores da a taxa de transmissão maxima de vídeo, áudio e dados e a capacidade do canal. O valor da capacidade do canal é sempre maior que zero.

Formato de saída

A quantidade máxima de dados a ser transmitido.

'''

tVideo = float(input())
tAudio = float(input())
tDados = float(input())
capacidade = float(input())
qdMax = (tVideo*5.2 + tAudio*3.4 + tDados*1.5) / capacidade
print ("%.2f" % qdMax)