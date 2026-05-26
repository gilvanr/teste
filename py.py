Exercícios Resolvidos em Python
Nível Fácil
1 - Soma dos números pares
try:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    soma = 0

    for numero in numeros:
        if numero % 2 == 0:
            print(f"{numero} é par")
            soma += numero

    print("Soma dos pares:", soma)

except Exception as erro:
    print("Erro:", erro)
2 - Verificar fruta na lista
try:
    frutas = ["maçã", "banana", "uva", "laranja", "abacaxi"]

    fruta = input("Digite uma fruta: ").lower()

    if fruta in frutas:
        print("Fruta encontrada!")
    else:
        print("Fruta não encontrada!")

except Exception as erro:
    print("Erro:", erro)
3 - Crescimento populacional
try:
    paisA = 80000
    paisB = 200000

    anos = 0

    while paisA < paisB:
        paisA += paisA * 0.03
        paisB += paisB * 0.015
        anos += 1

    print("Anos necessários:", anos)

except Exception as erro:
    print("Erro:", erro)
4 - Intervalo entre dois números
try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if n1 < n2:
        for i in range(n1, n2 + 1):
            print(i)
    else:
        for i in range(n2, n1 + 1):
            print(i)

except ValueError:
    print("Digite apenas números inteiros!")
5 - Tabuada
try:
    numero = int(input("Digite um número de 1 a 10: "))

    if 1 <= numero <= 10:
        print(f"\nTabuada de {numero}")

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    else:
        print("Número inválido!")

except ValueError:
    print("Digite um número inteiro!")
6 - Cálculo de H
try:
    n = int(input("Digite o valor de N: "))

    h = 0

    for i in range(1, n + 1):
        h += 1 / i

    print("Valor de H:", h)

except ValueError:
    print("Digite um número inteiro!")
Nível Médio
1 - Média dos alunos
try:
    notas = [
        [7.0, 8.5, 6.0],
        [9.0, 9.5, 10.0],
        [5.0, 4.0, 7.5]
    ]

    for i in range(len(notas)):
        media = sum(notas[i]) / len(notas[i])

        print(f"Aluno {i+1} -> Média: {media:.2f}")

        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

except Exception as erro:
    print("Erro:", erro)
2 - Lista sem duplicatas
try:
    lista = [1, 5, 2, 8, 3, 5, 1, 9, 2]
    nova_lista = []

    numero = int(input("Digite um número: "))

    if numero in lista and numero not in nova_lista:
        nova_lista.append(numero)

    print("Lista original:", lista)
    print("Nova lista:", nova_lista)

except ValueError:
    print("Digite um número válido!")
3 - Maior e menor número
try:
    numeros = []

    for i in range(15):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    maior = max(numeros)
    menor = min(numeros)

    print("Maior número:", maior)
    print("Posição:", numeros.index(maior))

    print("Menor número:", menor)
    print("Posição:", numeros.index(menor))

except ValueError:
    print("Digite apenas números!")
4 - Validação de dados
try:
    nome = input("Nome: ")

    if len(nome) <= 3:
        print("Nome inválido!")

    idade = int(input("Idade: "))

    if idade < 0 or idade > 150:
        print("Idade inválida!")

    salario = float(input("Salário: "))

    if salario <= 0:
        print("Salário inválido!")

    sexo = input("Sexo (f/m): ").lower()

    if sexo not in ["f", "m"]:
        print("Sexo inválido!")

    estado = input("Estado civil (s/c/v/d): ").lower()

    if estado not in ["s", "c", "v", "d"]:
        print("Estado civil inválido!")

    print("\nDados informados corretamente!")

except ValueError:
    print("Erro nos dados digitados!")
Nível Difícil
1 - Multiplicação de matrizes
try:
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    if len(A[0]) != len(B):
        print("Multiplicação impossível!")
    else:
        resultado = []

        for i in range(len(A)):
            linha = []

            for j in range(len(B[0])):
                soma = 0

                for k in range(len(B)):
                    soma += A[i][k] * B[k][j]

                linha.append(soma)

            resultado.append(linha)

        print("Resultado:")
        for linha in resultado:
            print(linha)

except Exception as erro:
    print("Erro:", erro)
2 - Jogo da Velha
try:
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    for jogada in range(9):
        simbolo = input("Digite X ou O: ").upper()

        linha = int(input("Linha (0-2): "))
        coluna = int(input("Coluna (0-2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = simbolo
        else:
            print("Posição ocupada!")

    for linha in tabuleiro:
        print(linha)

    vencedor = None

    # linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            vencedor = tabuleiro[i][0]

    # colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            vencedor = tabuleiro[0][i]

    # diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        vencedor = tabuleiro[0][0]

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        vencedor = tabuleiro[0][2]

    if vencedor:
        print("Vencedor:", vencedor)
    else:
        print("Deu velha!")

except Exception as erro:
    print("Erro:", erro)
3 - Palíndromos
try:
    palavras = []
    palindromos = []

    def verificar_palindromo(palavra):
        return palavra == palavra[::-1]

    for i in range(10):
        palavra = input(f"Digite a {i+1}ª palavra: ").lower()
        palavras.append(palavra)

    for palavra in palavras:
        if verificar_palindromo(palavra):
            palindromos.append(palavra)

    print("Palíndromos:", palindromos)

except Exception as erro:
    print("Erro:", erro)
4 - Validar endereços IP
try:
    entrada = [
        "200.135.80.9",
        "192.168.1.1",
        "8.35.67.74",
        "257.32.4.5",
        "85.345.1.2",
        "1.2.3.4",
        "9.8.234.5",
        "192.168.0.256"
    ]

    validos = []
    invalidos = []

    for ip in entrada:
        partes = ip.split(".")

        valido = True

        if len(partes) != 4:
            valido = False
        else:
            for parte in partes:
                if not parte.isdigit():
                    valido = False
                    break

                numero = int(parte)

                if numero < 0 or numero > 255:
                    valido = False
                    break

        if valido:
            validos.append(ip)
        else:
            invalidos.append(ip)

    print("[Endereços válidos:]")
    for ip in validos:
        print(ip)

    print("\n[Endereços inválidos:]")
    for ip in invalidos:
        print(ip)

except Exception as erro:
    print("Erro:", erro)
