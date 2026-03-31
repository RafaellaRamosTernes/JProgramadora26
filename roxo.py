# Definindo os códigos de cores
ROXO = "\033[35m"
AZUL = "\033[34m"
RESET = "\033[0m"

# A pergunta (input) terá a cor roxa
# O RESET ao final garante que o que o usuário digitar não fique roxo também
idade = float(input(f"{ROXO}Digite a sua idade: {RESET}"))

# As respostas (print) terão a cor azul
if idade >= 60:
    print(f"{ROSA}Idoso{RESET}")
elif idade >= 18:
    print(f"{AZUL}Adulto{RESET}")
elif idade >= 12:  # Ajustei a lógica aqui para permitir a categoria Criança
    print(f"{AZUL}Adolescente{RESET}")
else:
    print(f"{AZUL}Criança{RESET}")