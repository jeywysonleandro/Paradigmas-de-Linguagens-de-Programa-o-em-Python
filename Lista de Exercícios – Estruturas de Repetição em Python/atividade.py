#1. Contagem de 1 a 10

for i in range(1, 11):
    print(i)

#2.Números pares

n = 2
while n <= 50:
    print(n)
    n += 2

#3.Tabuada

n = int(input("Digite um número: "))
for i in range(1, 11):
 print(n, 'x', i, '=', n * i)

 #4.Soma de 1 a 100

 soma = 0
for i in range(1, 101):
 soma += i
print("Soma:", soma)

#5.Contagem regressiva

for i in range(10, -1, -1):
 print(i)
print("Fogo!")

#6.Impressão de caracteres

for letra in "Programação":
 print(letra)

 #7.Média de notas

notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(5)]
media = sum(notas)/5
print("Média:", media)

#8.Maior número digitado

maior = None
for i in range(10):
 n = float(input("Digite um número: "))
if maior is None or n > maior:
 maior = n
print("Maior número:", maior)

#9.Senha correta

senha_correta = "1234"
senha = ""
while senha != senha_correta:
 senha = input("Digite a senha: ")
print("Senha correta!")

#10.Contar vogais

palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
cont = 0
for letra in palavra:
 if letra in vogais:
  cont += 1
print("Número de vogais:", cont)

#11.Multiplicação acumulada

resultado = 1
for i in range(5):
 n = float(input("Digite um número: "))
resultado *= n
print("Resultado da multiplicação:", resultado)

#12.Número primo

num = int(input("Digite um número: "))
primo = True
if num < 2:
 primo = False
for i in range(2, num):
 if num % i == 0:
  primo = False
 break
if primo:
 print("Número primo")
else:
 print("Não é primo")

#13.Quadrados perfeitos

for i in range(1, 21):
 print(i, "ao quadrado é", i**2)

 #14.Fatorial

 n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n+1):
 fatorial *= i
print("Fatorial:", fatorial)

#15.Sequêncial de Fibonacci

a, b = 0, 1
for _ in range(15):
 print(a)
a, b = b, a + b

#16.Números Ímpares

limite = int(input("Digite o limite: "))
for i in range(1, limite+1, 2):
 print(i)

 #17.Adivinhação

 import random
n = random.randint(1, 20)
palpite = 0
while palpite != n:
 palpite = int(input("Adivinhe o número (1-20): "))
print("Parabéns! Você acertou.")