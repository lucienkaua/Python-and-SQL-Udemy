def dobro(x):
    return x * 2

lista = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, lista)
print(list(valor_dobrado))