# questao 1

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"Soma: {soma}")
print(f"subtracao: {subtracao}")
print(f"multiplicacao: {multiplicacao}")
(f"divisao: {divisao}")

# questao 2

c = float(input("Digite a temperatura em Celsius: "))
f = c * 9/5 + 32
k = c + 273.15

print(f"Fahrenheit: {f}")
print(f"Kelvin: {k}")

# questao 3

base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))
area = base * altura
perimetro = 2 * (base + altura)

print(f"Área: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")

# questao 4

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"sua média é: {media}")

# questao 5

a = input("Digite o primeiro valor: ")
b = input("Digite o segundo valor: ")

a, b = b, a

print("Valores invertidos: ")
print(a)
print(b)

# questao 6

C = float(input("Capital inicial: "))
i = float(input("Taxa de juros (%) ")) / 100
t = float(input("Tempo  (meses): "))

print(f"Juros: {C * i * t:.2f}")
print(f"Montante final: {C * (1 + i * t):.2f}")

# questao 7

distancia = float(input("Distância percorrida (km): "))
litros = float(input("Combustível gasto (litros): "))
try:
    consumo = distancia / litros
    saida = f"Consumo médio: {consumo:.2f} km/l"
except ZeroDivisionError:
    saida = "Não é possível calcular consumo: combustível gasto é 0"
print(saida)

# Questão 8

anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))
total_dias = anos * 365 + meses * 30 + dias
print(f"Idade total em dias: {total_dias} dias")

# Questão 9 

valor_original = float(input("Valor original da compra: R$ "))
percent = float(input("Percentual de desconto (%): "))
desconto = valor_original * (percent / 100)
valor_final = valor_original - desconto
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

# Questão 10 

distancia = float(input("Distância percorrida (km): "))
tempo = float(input("Tempo gasto (horas): "))
try:
    velocidade_media = distancia / tempo
    saida = f"Velocidade média: {velocidade_media:.2f} km/h"
except ZeroDivisionError:
    saida = "Não é possível calcular velocidade média: tempo = 0"
print(saida)
