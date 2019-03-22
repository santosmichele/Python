

pi = 3.14
raio1 = float(input())
raio2 = float(input())

area1 = pi*(raio1**2)
area2 = pi*(raio2**2)
if (area1 > area2):
    print ("Primeiro circulo")
elif(area1 < area2):
    print ("Segundo circulo")
else:
    print ("Iguais")
