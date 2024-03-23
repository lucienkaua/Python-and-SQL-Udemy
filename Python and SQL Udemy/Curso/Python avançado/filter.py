def par(i):
    if i % 2 == 0:
        return i

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(par, lista)
print(list(pares))