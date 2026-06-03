m = int(input("Digite o número de linhas (m): "))
n = int(input("Digite o número de colunas (n): "))

matriz = []

print(f"\nDigite os {m * n} elementos da matriz {m}x{n}:")
for i in range(m):
    linha = []
    for j in range(n):
        elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

transposta = []
for j in range(n):
    nova_linha = []
    for i in range(m):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

print("\nMatriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)