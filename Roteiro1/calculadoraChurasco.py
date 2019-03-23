###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################


totalChurasco = totalCarneBovina = totalCarneSuina = totalFrango = totalCerveja = totalRefrigerante = 0

# A opção para as carnes
tipoChurrasco = input()
tipoChurrasco = tipoChurrasco.upper()

if (tipoChurrasco not in ['C', 'BF', 'BS']):
    print ("Opção inválida.")
else:
    # Se o cliente quer pão de alho
    paoDeAlho = input()
    # Se o cliente quer bebidas para adultos
    bebidasAdulto = input()
    # Se o cliente quer bebidas para crianças
    bebidasCrianca = input()
    # A quantidade de crianças
    qntCrianca = int(input())
    # A quantidade de adultos
    qntAdulto = int(input())

    # Se o churrasco for completo:
    # 200g de carne bovina por adulto
    # 100g de carne de frango por adulto
    # 100g de carne suína por adulto
    # 200g de carne bovina por criança
    if (tipoChurrasco == 'C' ):
        totalCarneBovina = qntAdulto*200 + qntCrianca*200
        totalCarneSuina = totalFrango = qntAdulto*100
        totalCarneBovina /= 1000
        totalCarneBovina *= 32
        totalCarneSuina /= 1000
        totalCarneSuina *= 15
        totalFrango *= 18
        totalFrango /= 1000
    
    # Se o churrasco for BF:
    # 250g de carne bovina por adulto
    # 150g de carne de frango por adulto
    # 200g de carne bovina por criança
    elif (tipoChurrasco == 'BF' ):
        totalCarneBovina = qntAdulto*250 + qntCrianca*200
        totalFrango = qntAdulto*150
        totalCarneBovina /= 1000
        totalCarneBovina *= 32
        totalFrango *= 18
        totalFrango /= 1000

    # 250g de carne bovina por adulto
    # 150g de carne suína por adulto
    # 200g de carne bovina por criança
    elif (tipoChurrasco == 'BS' ):
        totalCarneBovina = qntAdulto*250 + qntCrianca*200
        totalCarneSuina = qntAdulto*150
        totalCarneBovina /= 1000
        totalCarneBovina *= 32
        totalCarneSuina /= 1000
        totalCarneSuina *= 15

    # Para qualquer tipo de churrasco
    # 2 garrafas de cerveja por adulto se ele quiser bebidas para adultos
    # 0,5 garrafas de refrigerante por criança se ele quiser bebidas para crianças
    if (bebidasAdulto == 'S'):
        totalCerveja = qntAdulto*2
        totalCerveja *= 8
    if (bebidasCrianca == 'S'):
        totalRefrigerante = qntCrianca*0.5
        totalRefrigerante *= 6

    # A carne bovina custa R$ 32,00 por Kg
    # Carne de frango custa R$ 18,00 por Kg
    # Carne suína custa R$ 15,00 por Kg
    # 1 garrafa de cerveja custa R$ 8,00
    # 1 garrafa de refrigerante custa R$ 6,00
    totalChurasco += totalCarneBovina + totalCarneSuina + totalFrango + totalCerveja + totalRefrigerante
    if (paoDeAlho == 'N'):
        totalChurasco -= totalChurasco*0.02
    print ("R$: %.2f" %totalChurasco)



