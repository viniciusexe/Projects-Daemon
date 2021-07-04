a = float(input("Votos Brancos: "))
b = float(input('Votos Nulos: '))
c = float(input('Votos Validos: '))
d = float(input('Total De Votos: '))

brancos = ((100 * a) / d)
nulos = ((100 * b) / d)
validos = ((100 * c) / d)

print('Votos Brancos: {}%'. format(brancos))
print('Votos Nulos: {}%'. format(nulos))
print('Votos validos: {}%'. format(validos))