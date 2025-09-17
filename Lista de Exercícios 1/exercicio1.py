print("Alunos - PLP Unifavip 2022.2")

num = input("Digite um número: ")
print("O número informado foi", num)
     

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print("A soma é:", a + b)
     

notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(4)]
print("Média =", sum(notas)/4)
     

metros = float(input("Digite metros: "))
print("Centímetros =", metros*100)
     

import math
raio = float(input("Digite o raio do círculo: "))
print("Área =", math.pi * raio**2)
     

lado = float(input("Digite o lado do quadrado: "))
area = lado**2
print("Área =", area, "Dobro =", area*2)
     

hora = float(input("Quanto ganha por hora: "))
horas = float(input("Horas no mês: "))
print("Salário =", hora*horas)
     

F = float(input("Temperatura em Fahrenheit: "))
C = 5 * ((F-32)/9)
print("Celsius =", C)
     

C = float(input("Temperatura em Celsius: "))
F = (C*9/5)+32
print("Fahrenheit =", F)
     

n1 = int(input("Primeiro inteiro: "))
n2 = int(input("Segundo inteiro: "))
n3 = float(input("Número real: "))
print("Produto:", (2*n1)*(n2/2))
print("Soma:", (3*n1)+n3)
print("Cubo:", n3**3)
     

h = float(input("Digite sua altura: "))
print("Peso ideal =", (72.7*h)-58)
     

h = float(input("Digite sua altura: "))
sexo = input("Digite M para homem ou F para mulher: ").upper()
if sexo == "M":
    print("Peso ideal =", (72.7*h)-58)
else:
    print("Peso ideal =", (62.1*h)-44.7)
     

peso = float(input("Peso de peixes (kg): "))
excesso = max(0, peso-50)
multa = excesso*4
print("Excesso:", excesso, "Multa: R$", multa)

     

hora = float(input("Quanto ganha por hora: "))
horas = float(input("Horas no mês: "))
bruto = hora*horas
ir = bruto*0.11
inss = bruto*0.08
sind = bruto*0.05
liquido = bruto - ir - inss - sind
print(f"+ Salário Bruto : R${bruto:.2f}")
print(f"- IR (11%) : R${ir:.2f}")
print(f"- INSS (8%) : R${inss:.2f}")
print(f"- Sindicato (5%) : R${sind:.2f}")
print(f"= Salário Líquido : R${liquido:.2f}")
     

area = float(input("Área em m²: "))
litros = area/3
latas = math.ceil(litros/18)
print("Latas:", latas, "Preço: R$", latas*80)
     

area = float(input("Área em m²: "))
litros = (area/6)*1.1  # com 10% de folga
latas = math.ceil(litros/18)
galoes = math.ceil(litros/3.6)
print("Só latas:", latas, "Preço: R$", latas*80)
print("Só galões:", galoes, "Preço: R$", galoes*25)
     
tamanho = float(input("Arquivo em MB: "))
velocidade = float(input("Velocidade em Mbps: "))
tempo = (tamanho/(velocidade/8))/60
print("Tempo aprox.:", tempo, "minutos")
     

vetor = [int(input("Digite um número: ")) for _ in range(5)]
num = int(input("Número para pesquisar: "))
if num in vetor:
    print("Encontrado na posição:", vetor.index(num))
else:
    print("Não existe.")
     

gabarito = ("A","B","C","D","E","A","B","C","D","E","A","B","C","D","E","A","B","C","D","E")
while True:
    respostas = [input(f"Questão {i+1}: ").upper() for i in range(20)]
    acertos = sum(1 for i in range(20) if respostas[i]==gabarito[i])
    print("Acertos:", acertos)
    if acertos >= 12: print("Classificado")
    else: print("Desclassificado")
    if input("Cadastrar outro aluno? (S/N): ").upper()=="N": break
     

cidades = []
while len(cidades)<6:
    nome = input("Digite nome da cidade: ")
    if nome in cidades:
        print("Cidade repetida! Digite outra.")
    else:
        cidades.append(nome)
print("Cidade mais longa:", max(cidades, key=len))
     

letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")
     

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
if media==10: print("Aprovado com Distinção")
elif media>=7: print("Aprovado")
else: print("Reprovado")
     

p1,p2,p3 = input("Digite 3 palavras separadas por espaço: ").split()
maior = max([p1,p2,p3], key=len)
print("Maior palavra:", maior, "com", len(maior), "caracteres")
     

nums = [float(input("Número: ")) for _ in range(3)]
print("Maior:", max(nums), "Menor:", min(nums))
     

precos = [float(input(f"Preço produto {i+1}: ")) for i in range(3)]
print("Comprar o de R$", min(precos))
     

nums = sorted([float(input("Número: ")) for _ in range(3)], reverse=True)
print(nums)
     

turno = input("Digite M/V/N: ").upper()
if turno=="M": print("Bom Dia!")
elif turno=="V": print("Boa Tarde!")
elif turno=="N": print("Boa Noite!")
else: print("Valor Inválido!")
     

sal = float(input("Salário atual: "))
if sal<=280: perc=0.20
elif sal<=700: perc=0.15
elif sal<=1500: perc=0.10
else: perc=0.05
aumento = sal*perc
print("Antes:", sal, "Percentual:", perc*100,"%", "Aumento:", aumento, "Novo:", sal+aumento)
     

hora = float(input("Valor hora: "))
horas = float(input("Horas no mês: "))
bruto = hora*horas
if bruto<=900: ir=0
elif bruto<=1500: ir=bruto*0.05
elif bruto<=2500: ir=bruto*0.10
else: ir=bruto*0.20
inss = bruto*0.10
fgts = bruto*0.11
sind = bruto*0.03
descontos = ir+inss+sind
print("Bruto:", bruto)
print("(-) IR:", ir)
print("(-) INSS:", inss)
print("(-) Sindicato:", sind)
print("FGTS:", fgts)
print("Descontos:", descontos)
print("Líquido:", bruto-descontos)
     

perguntas = ["Telefonou para a vítima?","Esteve no local?","Mora perto?","Devia para a vítima?","Já trabalhou com a vítima?"]
resp = [input(p+" (S/N): ").upper()=="S" for p in perguntas]
cont = sum(resp)
if cont==2: print("Suspeita")
elif cont in [3,4]: print("Cúmplice")
elif cont==5: print("Assassino")
else: print("Inocente")
     

for i in range(13):
    nome = input("Nome: ")
    mat = input("Matrícula: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1+n2)/2
    print("Matrícula:", mat, "Nome:", nome, "Média:", media)
     

pessoas = []
while True:
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    cpf = input("CPF: ")
    sexo = input("Sexo: ")
    pessoas.append((nome,altura,peso,cpf,sexo))
    if input("Cadastrar mais? (S/N): ").upper()=="N":
        break
busca = input("Digite CPF para buscar: ")
for p in pessoas:
    if p[3]==busca:
        imc = p[2]/(p[1]**2)
        print("Nome:",p[0],"IMC:",imc)
     