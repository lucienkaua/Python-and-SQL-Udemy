# 01
seq1 = input("Digite a sequência: ")
seq2 = input("Digite a sequência: ")

import re

busca = re.match(seq1, seq2)
if busca:
    print("Sequências iguais encontradas.")
    print(busca.group())
else:
    print("Sequências diferentes.")

# Adicionais do módulo RE
seq1 = "AT.GM*" # O . idêntifica toda a sequência sem se importar com qual o caractere que esteja no lugar do ponto. O * significa que o caractere que o precede pode se repetir e isso vai indicar que o mesmo assim pertence a busca.
seq2 = "ATBGMMMMM"

import re

busca = re.match(seq1, seq2)
if busca:
    print("Sequências iguais encontradas.")
    print(busca.group())
else:
    print("Sequências diferentes.")
