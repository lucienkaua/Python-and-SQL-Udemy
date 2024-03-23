lista = ["Arroz", "Feijão", "Frango", "Ovos"]

for i in range(len(lista)):
    print(i, lista[i])

# Usando enumerate
for i, nome in enumerate(lista):
    print(i, nome)
