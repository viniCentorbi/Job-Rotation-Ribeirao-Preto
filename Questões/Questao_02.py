def fibonacci(numero):
	penultimo = 0
	ultimo = 1

	#pertence recebe falso para no caso de um número negativo ser inserido
	pertence = False

	#Fará a sequência de Fibonacci até o número inserido
	while penultimo <= numero:

		#Verifica se o número pertence a sequência
		if numero == penultimo or numero == ultimo:
			pertence = True			
		else:
			pertence = False

		#O próximo número da sequência vai receber a soma do último e penúltimo
		proximo = penultimo + ultimo

		#O último passa a ser o penúltimo
		penultimo = ultimo

		#E o próximo passar a ser o último
		ultimo = proximo

	return pertence


if fibonacci(377):
	print('Pertence a sequência!')
else:
	print('Não pertence a sequência!')
