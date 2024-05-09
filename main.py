import random

naipes = ['Ouros', 'Copas', 'Espadas', 'Paus']
números = ['Á', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'Q','k']

cartas = []
#for para naipes
for i in range(4):
  #for para números 
  for u in range(13):
    cartas.append(str(números[u])+" de "+naipes[i])

quantidade = int(input("Digite a quantidade de cartas"))

random.shuffle(cartas)
for i in range(quantidade):
  print(cartas[i])
  