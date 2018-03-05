#/usr/bin/python3.6

aux, votacao, candidatos, limite, i = '',[],[],0,0

print("Definição do pleito: ")
limite = int(input())
while (i < limite):
	candidatos.append(input())
	i += 1
print()
print("Votação:")
while True:
	aux = input()
	for nome in candidatos:
		if aux.lower() != nome.lower():
			break
		else:
			votacao.append(aux)
print("Candidatos:",candidatos)
print("Votação:",votacao)
print()
for nome in candidatos:
	print("%s com %s voto(s)" % (nome,candidatos.lower().count(nome)))
