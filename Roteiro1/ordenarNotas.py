notas = []
for x in range (0,3):
    notas.append(int(input()))

notas = sorted(notas)

for x in range (0,3):
    print (int(notas[x])) 