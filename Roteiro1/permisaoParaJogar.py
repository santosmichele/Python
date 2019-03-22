# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

jogosValidos = ['azar', 'mmorpg', 'moba', 'casual']
idadesValidas = [21, 32 , 14, 10]
idadeJogador = int(input())
jogoDesejado = input()

if (idadeJogador > 0 and idadeJogador < 130):
    if (jogoDesejado in jogosValidos):
        for indice, valor in enumerate(jogosValidos):
            if (valor == jogoDesejado):
                if (idadeJogador < idadesValidas[indice]):
                    print ("Volte daqui há alguns anos.")
                    break
                else:
                    print ("Pode entrar!")
                    break
    else:
        print ("Jogo invalido.")
else:
    print ("Idade invalida.")