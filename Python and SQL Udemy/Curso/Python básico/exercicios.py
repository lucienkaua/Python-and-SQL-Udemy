# 01
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
# Resposta sem mudança de código


# 02
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1+n2)/2

if media >= 6:
    print(f"Você foi aprovado com média {media}!")
else:
    print("Você não foi aprovado.")
# Resposta sem mudança de código

# 03
import math
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"X1 = {x1}\nX2 = {x2}")
# Resposta sem mudança de código

# 04
lista = [3, 6, 1]
for i in range(len(lista)):
    for j in range(0, len(lista)-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(lista)
# Resposta
lista = [3,2,1]
print(sorted(lista)) # Isso para exibir a função
print(lista.sort(reverse=True))  # Isso para exibir o método - parâmetro reverse ativado, lista ordenada de forma decrescente

#05
resultado = int
n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
operador = str(input("""Digite o símbolo da operação que deseja realizar.\n
                     [+] Adição\n
                     [-] Subtração\n
                     [*] Multiplicação\n
                     [/] Divisão\n
                     Sua opção >>> """)).strip()
if operador == "+":
    resultado = n1 + n2
    print(f"{n1} somado a {n2} é igual a {resultado}")
elif operador == "-":
    resultado = n1 - n2
    print(f"{n1} subtraido de {n2} é igual a {resultado}")
elif operador == "*":
    resultado = n1 * n2
    print(f"{n1} multiplicado por {n2} é igual a {resultado}")
elif operador == "/":
    resultado = n1 / n2
    print(f"{n1} dividido por {n2} é igual a {resultado}")
else:
    print("Esse não é um operador válido.")
# Resposta sem mudança de código