

cod = int (input())
if (cod == 1) :
    print ("Nordeste")
elif (cod == 2) :
    print ("Norte")
elif (cod == 3 or cod == 4) :
    print ("Centro-Oeste")
elif (cod >= 5 and cod <= 9) :
    print ("Sul")
else: 
    print ("Sudeste")