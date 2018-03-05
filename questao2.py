#!/usr/bin/python3
def contaVogais(palavra):
    total = 0
    
    for letra in palavra:
        if letra in "aeiouAEIOU":
           total += 1
    return total

def maiorPalavra(lista):
	tam,maior = 0,''
	
	for x in lista:
		if len(x) > tam:
			tam = len(x)
			maior = x
	return maior

def contaPalindromos(lista):
    total = 0
    
    for p in lista:
        if p == p[::-1]:
           total += 1
    
    return total

def main():
	palavras,totalVogais,totalDigitos,aux = [],0,0,'teste'
	
	while(aux != ''):
		print("Para encerrar, aperte a tecla <enter>.")
		aux = input("Digite alguma coisa: ")
		
		if aux != '':
			totalVogais += contaVogais(aux)
			totalDigitos += len(aux)
			palavras.append(aux)
	
	print()
	print("============== RELATÓRIO ==============")
	print()
	print("Palavras:",palavras)
	print()
	print("Total de vogais:",totalVogais)
	print()
	print("Total de dígitos:",totalDigitos)
	print()
	print("Maior palavra digitada:",maiorPalavra(palavras))
	print()
	print("Quantidade de palavras palíndromas:",contaPalindromos(palavras))

if __name__ == '__main__':
	main()