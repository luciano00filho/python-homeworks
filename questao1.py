#!/usr/bin/python3
def main():
	aux,i,n = 0,0,[] # variáveis

	while(aux >= 0):
		print("Para encerrar, digite um número negativo.")	
		aux = int(input("Digite um número: "))
		
		# mantenho somente os 6 primeiros números em memória
		if (i < 6):
			n.append(aux)
		elif (i >= 6 and aux >= 0):
			print("Este número será descartado (",aux,").")
		
		i += 1

	print() # linha em branco	

	if len(n) < 5:
		print("Números lidos:",n)
	else:
		n.sort(reverse=True) # ordeno a lista de números do maior para o menor
		print("5 maiores números informados:",n[:5]) # mostro os 5 primeiros números da lista ordenada

if __name__ == '__main__':
	main()