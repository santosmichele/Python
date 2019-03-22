'''
Descrição
Escreva um programa que solicite ao usuário:

Sua temperatura
Se está tendo secreção, tosse e dor no corpo (“S” ou “N”)
Após a solicitação dos dados:

Caso a temperatura seja maior ou igual a 37 graus e as demais respostas sejam iguais a “S”, uma mensagem “Exames Especiais” deve ser exibida.
Caso a temperatura seja maior ou igual a 37 graus e as demais respostas sejam iguais a “N”, uma mensagem “Exames Basicos” deve ser exibida.
Caso a temperatura seja menor do que 37 graus e não houver secreção, tosse e dor no corpo, a mensagem será “Liberado”.
Caso a temperatura seja inferior a 37 graus, mas houver dor no corpo, tosse e secreção, a mensagem deve ser igual a “Exames Básicos”.
Se, ao perguntar se o usuário está com secreção, tosse e dor no corpo, ele responder algo diferente de "S" ou "N", exiba uma mensagem de erro.

Formato de entrada

A temperatura do paciente (entre 35 e 41 graus)

Se está tendo secreção, tosse e dor no corpo ("S" ou "N")

Formato de saída

"Exames Especiais", caso a temperatura seja maior que 37 graus e ele esteja com secreção, tosse e dor.

"Exames Basicos", caso a temperatura seja menor que 37 graus e ele esteja com secreção, tosse e dor.

"Liberado", caso a temperatura seja maior que 37 graus e ele não esteja com secreção, tosse e dor.

Se, ao perguntar se o usuário está com secreção, tosse e dor no corpo, ele responder algo diferente de "S" ou "N", exiba a mensagem "Erro".
 or

'''

temperatura = float (input())
sintomas = input()

if not( (sintomas == 'S' or sintomas == 'N') and (temperatura >=35 and temperatura <=41  ) ):
    print ("Erro")
elif ( temperatura >= 37 and sintomas == 'S' ):
    print ("Exames Especiais")
elif ( (temperatura <= 37 and sintomas == 'S') or  (temperatura >= 37 and sintomas == 'N' ) ):
    print ("Exames Basicos")
else:
    print ("Liberado")