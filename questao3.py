#/usr/bin/python3.6

aux, votacao, candidatos, limite, i, repetir = '', [], [], 0, 0, True

print("Definição do pleito: ")
limite = int(input())
while (i < limite):
	candidatos.append(input())
	i += 1
print()
print("Votação:")

while (repetir):


print("Candidatos:",candidatos)
print("Votação:",votacao)
print()
for nome in candidatos:
	print("%s com 0 voto(s)" % (nome)
