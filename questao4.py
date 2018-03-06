#/usr/bin/python3.6
import sys

def main():
	dimensao, intervalo, matrix, rows, cols, vmin, vmax = '','',[[]],0,0,0,0
	
	dimensao = input("Qual o tamanho da matriz? ").split()
	rows = int(dimensao[0]) # linhas
	cols = int(dimensao[1]) # colunas

	intervalo = input("Qual o intervalo de valores? ").split()
	vmin = int(intervalo[0]) # mínimo
	vmax = int(intervalo[1]) # máximo

	# crio a matriz zerada
	matrix = [0.0] * rows
	for i in range(rows):
		matrix[i] = [0.0] * cols
	print(matrix)	

	# gero os números
	cont = 0
	listaNum = []
	for x in range(0,(rows * cols)):
		listaNum.append(x * 0.13)

	# modifico a matriz
	for i in range(rows):
		for j in range(cols):
			matrix[i][j] = listaNum[cont]
			cont += 1
	print(matrix)
			
if __name__ == '__main__':
	main()