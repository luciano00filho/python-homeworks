#/usr/bin/python3.6
import sys

def montaMatriz(linhas,colunas):
	matriz = [0.0] * linhas
	for i in range(linhas):
		matriz[i] = [0.0] * colunas
	return matriz

def geraNumeros(vmin,vmax,linhas,colunas):
	for x in range(vmin,(linhas * colunas),1):
		print("x1 =",x)

def main():
	dimension, interval, matrix, rows, cols, vmin, vmax, listaNum, cont = '','',[[]],0,0,0,0,[],0
	
	dimension = input("Qual o tamanho da matriz? ").split()
	rows = int(dimension[0]) # linhas
	cols = int(dimension[1]) # colunas

	interval = input("Qual o intervalo de valores? ").split()
	vmin = int(interval[0]) # mínimo
	vmax = int(interval[1]) # máximo

	# crio a matriz zerada
	matrix = montaMatriz(rows,cols)
	print("matrix =",matrix)
	
	# gero os números
	geraNumeros(vmin,vmax,rows,cols)
	sys.exit()
	
	# modifico a matriz
	for i in range(rows):
		for j in range(cols):
			print("cont =",cont)
			matrix[i][j] = listaNum[cont]
			cont += 1
	print(matrix)
			
if __name__ == '__main__':
	main()
