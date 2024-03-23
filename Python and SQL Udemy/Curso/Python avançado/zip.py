lista_1 = ["Sapo da Macadâmia", "Urubu do Pix", "Pantera cor de rosa"]
lista_2 = [1, 2, 3]
lista_3 = ["R$ 1.000,00", "R$ 10.000,00", "R$ 620,00"]

for i, animal, valor in zip(lista_2, lista_1, lista_3):
    print(i, animal, valor)
