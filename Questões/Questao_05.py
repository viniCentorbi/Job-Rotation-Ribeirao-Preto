len_string = len

def reverse_string(string):

	letras = []

	for char in string:

		letras.append(char)

	num_letras = len(letras)

	palavra = ''

	for i in range(num_letras):
		
		palavra = palavra + letras[num_letras-1]
		num_letras-=1

	print(palavra)

reverse_string('Escreva um programa que inverta os caracteres de um string')