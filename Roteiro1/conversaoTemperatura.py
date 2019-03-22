'''
Descrição
Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
Formato de entrada

Uma escala de medida de temperatura ("C", "F" ou "K")

Um valor de temperatura a ser convertido

Esse valor deve obedecer os seguintes valores mínimos (float):
Celsius: t >= -273.0
Fahrenheit: t >= -459,67
Kelvin: t >= 0.0
Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
"Valor de temperatura abaixo do minimo"
Não há limite máximo de temperatura


Formato de saída

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
"Valor de temperatura abaixo do minimo"
'''


escalaDeEntrada = input()
temperatura = float(input())
zeroKelvin = 273.15
msgErro = "Valor de temperatura abaixo do minimo"

if (escalaDeEntrada.upper() == 'C'):
    if (temperatura >= -273):
        converteParaF = (1.8*temperatura) +32
        converteParaK = temperatura + zeroKelvin
        print ("%.2f F\n%.2f K" % (converteParaF, converteParaK) ) 
    else:
        print (msgErro)
elif (escalaDeEntrada.upper() == 'F'):
    if (temperatura >= 459,67):
        converteParaC = (temperatura - 32) / 1.8
        converteParaK = converteParaC + zeroKelvin
        print ("%.2f C\n%.2f K" % (converteParaC, converteParaK) ) 
    else:
        print (msgErro)
elif (escalaDeEntrada.upper() == 'K'):
    if (temperatura >= 0):
        converteParaC = temperatura - zeroKelvin
        converteParaF = (1.8*(temperatura - zeroKelvin) +32)
        print ("%.2f C\n%.2f F" % (converteParaC, converteParaF) ) 
    else:
        print (msgErro)




