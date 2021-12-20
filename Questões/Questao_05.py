def reverse_string(string):

	letras = []

	#Percorre a string e adiciona cada caracterer na lista
	for char in string:

		letras.append(char)

	#Recebe o tamanho da lista
	num_letras = len(letras)

	palavra = ''
	indice = num_letras - 1

	#Percorre a lista de caracteres
	for i in range(num_letras):
		
		#Concatena os caracteres da lista do último elemento para o primeiro
		palavra = palavra + letras[indice]

		#Decrementa o valor do índice para acessar a lista de trás para frente
		indice-=1

	print(palavra)

reverse_string('Escreva um programa que inverta os caracteres de um string')
