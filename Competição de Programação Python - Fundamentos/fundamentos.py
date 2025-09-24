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