def fibonacci(numero):
	penultimo = 0
	ultimo = 1

	pertence = False

	while penultimo <= numero:

		if numero == penultimo or numero == ultimo:
			pertence = True
			break
		else:
			pertence = False

		proximo = penultimo + ultimo

		penultimo = ultimo
		ultimo = proximo

	return pertence


if fibonacci(377):
	print('Pertence a sequência!')
else:
	print('Não pertence a sequência!')
