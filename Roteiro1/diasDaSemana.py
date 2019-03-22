dia = int (input())
semana = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
if (dia >= 0 and dia <=7):
    print (semana[dia-1])
else:
    print ("valor invalido")