# Criando Tuplas
coordenadas = (10,20)
dias = ("segunda","terça","quarta","quinta","sexta")

# Acessando elementos
print("x:",coordenadas[0], "| Y:", coordenadas[1])

# Slicing (fatiamento) em tuplas
print("primeiros 3 dias", dias[:3])

# Tamanho
print("tamanho da tupla 'dias':",len(dias))

# Verificae se um elemento está na tupla
print("Tem 'segunda'?", "segunda" in dias)

# Contagem e Indice em Tuplas
print("Contagem de 'terça':", dias.count("terça"))
print("índice de 'quarta':", dias.index("quarta"))