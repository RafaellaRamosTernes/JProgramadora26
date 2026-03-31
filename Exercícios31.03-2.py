# Exercícios de 

# Número 1
num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Número 2
idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Número 3
idade = int(input("Informe sua idade: "))

if idade <= 11:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# Número 4 
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")

# Número 5
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O primeiro número ({n1}) é maior.")
elif n2 > n1:
    print(f"O segundo número ({n2}) é maior.")
else:
    print("Os números são iguais.")

# Número 6
num1 = float(input("Primeiro número: "))
operacao = input("Operação (+, -, /, *): ")
num2 = float(input("Segundo número: "))

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "/":
    resultado = num1 / num2
elif operacao == "*":
    resultado = num1 * num2

print("Resultado: " + str(resultado))