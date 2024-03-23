arquivo = open("mdl - python intermediário\\sequence.fasta")

linhas = arquivo.readlines()
multifasta = {}

for linha in linhas:
    if linha[0] == ">":
        seq_atual = linha[1:].strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] = multifasta[seq_atual] + linha.strip()

print(multifasta["""sp|P52407.2|E13B_HEVBR RecName: Full=Glucan endo-1,3-beta-glucosidase, basic vacuolar isoform; AltName: Full=(1-_3)-beta-glucan endohydrolase; Short=(1-_3)-beta-glucanase; AltName: Full=Beta-1,3-endoglucanase; AltName: Allergen=Hev b 2; Contains: RecName: Full=Glucan endo-1,3-beta-glucosidase minor form 3; Contains: RecName: Full=Glucan endo-1,3-beta-glucosidase minor form 2; Contains: RecName: Full=Glucan endo-1,3-beta-glucosidase minor form 1; Contains: RecName: Full=Glucan endo-1,3-beta-glucosidase major form; Flags: Precursor"""])
