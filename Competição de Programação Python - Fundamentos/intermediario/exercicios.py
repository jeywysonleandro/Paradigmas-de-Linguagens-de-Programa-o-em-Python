#11 Classificação de Notas

nota = int(input("Digite a nota (0 a 100): "))

if 90 <= nota <= 100:
    print("A")

elif 80 <= nota <= 89:
    print("B")

elif 70 <= nota <= 79:
    print("C")

elif 60 <= nota <= 69:
    print("D")

else:
    print("F")

# Questao 12 Maior de Três Números

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = a

if b > maior:
    maior = b

if c > maior :
    maior = c

    print("O maior número é:", maior)

#Questão 13 - Calculadora de IMC

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)

print(f"IMC = {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")

elif 18.5 <= imc <= 24.9:
    print("Normal")

elif 25 <= imc <= 29.9:
    print("Sobrepeso")

else:
    print("Obesidade")

#Questão 14 - Ano Bissexto

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não bissexto")

#Questão 15 - Tabuada Completa

n = int(input("Digite um número: "))

for i in range(1, 11):
    
    print(f"{n} x {i} = {n * i}")

#Questão 16 – Contagem de Números Pares

inicio = int(input("número inicial: "))
fim = int(input("número final: "))

pares = len([n for n in range(inicio, fim+1) if n % 2 == 0])
print(f"Quantidade de pares: {pares}")

#Questão 17 – Soma dos Primeiros N Números

n = int(input("Digite N: "))

print(f"Soma: {n * (n + 1) // 2 }")

#Questão 18 – Fatorial

n = int(input("Digite um número: "))
fat = 1

for i in range(2, n+1):
    fat *= i

print(f"Fatorial: {fat}")

#Questão 19 – Adivinhação de Número

import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Adivinhe o número (1 a 100): "))
    tentativas += 1

    if chute == numero:

        print(f"Acertou em {tentativas} tentativas!")
        break

    print("Maior" if chute < numero else "Menor")

#Questão 20 – Validador de Senha

senha = input("Digite a senha: ")

erros = []

if len(senha) < 8: erros.append("mínimo 8 caracteres")

if not any(c.isdigit() for c in senha): erros.append("precisa de número")

if not any(c.isupper() for c in senha): erros.append("precisa de maiúscula")

if not any(c.islower() for c in senha): erros.append("precisa de minúscula")

print("Senha válida" if not erros else f"Senha inválida: {', '.join(erros)}")

