nome_arq = str(input("Insira o nome do arquivo: "))
arquivo = open(f"mdl - python intermediário\\{nome_arq}")
linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())
arquivo.close()
