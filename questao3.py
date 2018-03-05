#/usr/bin/python3.6
def procuraNome(nome,lista,contagem=False):
	auxLista = []
	
	# criar a lista auxiliar
	for n1 in lista:
		auxLista.append(n1.lower())

	if (contagem): # faço a contagem dos votos
		return auxLista.count(nome.lower())
	else: # verifico se o nome votado é válido
		if nome.lower() not in auxLista:
			return False
	
	return True		

def main():
	aux, votacao, candidatos, limite, i, parada = '', [], [], 0, 0, True

	print("Definição do pleito:")
	limite = int(input())
	while (i < limite):
		candidatos.append(input())
		i += 1

	print()
	print("Votação:")
	while (parada):
		aux = input()
		parada = procuraNome(aux,candidatos)
		if (parada):
			votacao.append(aux)		
	# DEBUGGING
	# print("Candidatos:",candidatos)
	# print("Votação:",votacao)
	print()
	for nome in candidatos:
		print("%s com %d voto(s)" % (nome,procuraNome(nome,votacao,True)))

if __name__ == '__main__':
	main()