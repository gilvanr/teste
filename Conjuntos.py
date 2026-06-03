import random

def main():
    try:
        qtde = int(input("Digite a quantidade de elementos da lista (Qtde): "))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        return

    if qtde < 0:
        print("A quantidade deve ser um valor não negativo.")
        return

    lista = [random.randint(1, 100) for _ in range(qtde)]
    print("Lista original:", lista)

    vistos = set()
    sem_repetidos = []
    for num in lista:
        if num not in vistos:
            vistos.add(num)
            sem_repetidos.append(num)

    print("Lista sem repetidos:", sem_repetidos)
    print("Tamanho da nova lista:", len(sem_repetidos))

if __name__ == "__main__":
    main()