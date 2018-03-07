#/usr/bin/python3.6
pontos = ()

def lerPares():
	global pontos
	coord, px, py, vaux = '','','',()
	
	while True:
		coord = input("Informe um par de valores inteiros: ").split()
		px = int(coord[0])
		py = int(coord[1])
		
		# guardo os pares válidos
		if (px == 0 and py == 0):
			break
		else:
			vaux = px,py
		
		# monto a tupla de pontos
		pontos += vaux,

def contarPontos():
	print("(a)",len(pontos))

def mostrarPontosPorLinha():
	print("(b)")
	for i in pontos:
		print(i)

def distanciaEntrePontos(v1,v2):
	res = (((v1[0] - v2[0]) ** 2) + ((v1[1] - v2[1]) ** 2))
	sqrt = res ** (1/2)
	return sqrt

def pontosMaisProximos():
	print("(c)")
	
def pontosMaisDistantes():
	print("(d)")

def main():
	lerPares()
	contarPontos()
	mostrarPontosPorLinha()
	pontosMaisProximos()
	pontosMaisDistantes()

if __name__ == '__main__':
	main()