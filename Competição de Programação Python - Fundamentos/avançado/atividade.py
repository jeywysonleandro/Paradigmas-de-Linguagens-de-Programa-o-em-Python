#Questão 21 – Sequência de Fibonacci

n = int(input("Quantos números da Fibonacci? "))
a,b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a,b = b, a + b

#Questão 22 – Número Primo

num = int(input("Digite um número: "))
primo = True
if num < 2:
    primo = False
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        primo = False
        break
print("Primo" if primo else "Não primo")

#Questão 23 – Palíndromo

texto = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
if texto == texto[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")

#Questão 24 – Contador de Caracteres

from collections import Counter
texto = input("Digite uma string: ")
contagem = Counter(texto)
for char, freq in contagem.most_common():
    print(char, freq)


#Questão 25 – Jogo da Velha (Verificador)

tabuleiro = [input(f"Posição {i+1} (X/O): ") for i in range(9)]
vitorias = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]

for v in vitorias:
    if tabuleiro[v[0]] == tabuleiro[v[1]] == tabuleiro[v[2]] != "":
        print(tabuleiro[v[0]], "venceu")
        break
else:
    print("Empate" if "" not in tabuleiro else "Jogo em andamento")


#Questão 26 – Bubble Sort

lst = list(map(int, input("Lista: ").split()))
for i in range(len(lst)):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("Lista ordenada:", lst)

#Questão 27 – Calculadora de Expressões

expr = input("Digite uma expressão: ")
try:
    resultado = eval(expr)
    print("Resultado:", resultado)
except:
    print("Expressão inválida")

#Questão 28 – Gerador de Senhas

import random, string
tamanho = int(input("Tamanho da senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choice(caracteres) for _ in range(tamanho))
print("Senha gerada:", senha)


#Questão 29 – Conversor de Bases Numéricas

num = int(input("Número decimal: "))
print("Binário:", bin(num)[2:])
print("Octal:", oct(num)[2:])
print("Hexadecimal:", hex(num)[2:])


#Questão 30 – Sistema de Notas Estudantil

alunos = {}
while True:
    nome = input("Nome do aluno (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    notas = list(map(float, input("Notas separadas por espaço: ").split()))
    media = sum(notas)/len(notas)
    situacao = "Aprovado" if media >= 60 else "Reprovado"
    alunos[nome] = {"notas": notas, "média": media, "situação": situacao}

print("\nRelatório da turma:")
for nome, info in alunos.items():
    print(f"{nome} -> Notas: {info['notas']}, Média: {info['média']:.2f}, Situação: {info['situação']}")
