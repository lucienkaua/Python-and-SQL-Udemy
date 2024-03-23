seq = str(input("Insira a sequência: "))
nome_arq = str(input("Insira o nome do arquivo: "))
arquivo = open(nome_arq, "w")


arquivo.write("> seq\n")
arquivo.write(seq)
arquivo.close()
