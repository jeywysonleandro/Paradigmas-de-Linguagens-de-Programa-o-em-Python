#Questão 21 – Sequência de Fibonacci

n = int(input("Quantos números da Fibonacci? "))
a,b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a,b = b, a + b

#Questão 22 – Número Primo