#Exercícios dia 30/03
# número 1.
nome= input("Digite seu nome: ")
print(nome)
# número 2
idade= input("Digite sua idade: ")
print(idade)
# Número 3
nome= input("Digite seu nome: ")
print(nome)
cidade = input("Digite sua cidade:")
print(nome, "mora em", cidade)
# Número 4
numero = float(input("Digite um número: "))
print(f"O dobro é: {numero * 2}")
# Número 5
altura = float(input("Digite sua altura em metros (ex: 1.65): "))
print(f"Sua altura é {altura}m")
# Número 6
numero1 = int(input("Primeiro número inteiro: "))
numero2 = int(input("Segundo número inteiro: "))
print(f"A soma é: {numero1 + numero2}")
# Número 7
denominador1 = float(input("Primeiro valor: "))
denominador2 = float(input("Segundo valor: "))
print(f"A média é: {(denominador1 + denominador2) / 2}")
# Número 8
valor = input("Digite um número: ")
print(f"Antes: {type(valor)}")
valor_int = int(valor)
print(f"Depois: {type(valor_int)}")
# Número 9
preco = float(input("Preço do produto: "))
desconto = preco * 0.90
print(f"Preço com desconto: R$ {desconto:.2f}")
# Número 10
raio = float(input("Raio do círculo: "))
area = 3.14 * (raio ** 2)
print(f"A área do círculo é: {area:.2f}")
# Número 11
distancia = float(input("Distância (km): "))
tempo = float(input("Tempo (h): "))
print(f"Velocidade média: {distancia / tempo} km/h")
# Número 12
numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
numero3 = float(input("Número 3: "))
media = (numero1 + numero2 + numero3) / 3
print(f"Média: {media:.2f}")
# Número 13
salario = float(input("Salário atual: "))
aumento = float(input("Percentual de aumento: "))
novo_salario = salario + (salario * aumento / 100)
print(f"Novo salário: R$ {novo_salario:.2f}")
# Número 14
minutos = int(input("Quantidade de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos}min -> {horas}h{minutos_restantes:02d}")
# Número 15
nome = input("Nome: ")
idade = input("Idade: ")
print(f"Nome: {nome} | Idade: {idade} anos")
# Número 16
a = int(input("Valor A: "))
b = int(input("Valor B: "))
print(f"a + b = {a+b} | a - b = {a-b} | a * b = {a*b}")
# Número 17
valor = float(input("Digite um valor decimal: "))
print(f"{valor:.2f}")
# Número 18
nome = input("Nome do aluno: ")
nota = float(input("Nota: "))
print(f"Aluno {nome} ficou com nota {nota:.1f}")
# Número 19
nascimento = int(input("Ano de nascimento: "))
ano_atual = 2026 
print(f"Sua idade estimada em 2026 é: {ano_atual - nascimento} anos")


