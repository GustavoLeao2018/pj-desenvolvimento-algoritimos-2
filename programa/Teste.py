from Lista import Lista
from random import randint, choice, random
from lorem import sentence


lista = Lista()
for i in range(randint(10, 20)):
    lista.append(randint(0, 100))
    lista.append(random() * randint(0, 100))
    lista.append(sentence())

print(f"Lista: {lista.list_simple()}")
lista.mostra()
lista.imprime()
print(f"Ultimo item: {lista.final.dado}")
print(f"Tamanho: {lista.tamanho}")