menu = 0

def abrir_arquivo():
    nome = str(input("Digite o nome do arquivo: "))
    arquivo = open(nome, "r")
    return arquivo

def ler_arquivo(arquivo):
    linhas = arquivo.readlines()
    for linha in linhas: 
        print(linha.strip())

while menu != 3:
    menu = int(input("[1] Abrir arquivo\n[2] Ler arquivo aberto\n[3] Sair\nDigite a opção desejada: "))

    if menu == 1:
        arquivo = abrir_arquivo()
        print("O arquivo foi aberto.")
    elif menu == 2:
        ler_arquivo(arquivo)
    elif menu == 3:
        break
    else:
        print("Digite uma das opções válidas.")
        
arquivo.close()