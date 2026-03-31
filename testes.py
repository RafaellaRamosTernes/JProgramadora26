
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
