


def pesquisa(lista, item_busca, index=0):

    if index == len(lista):
        return -1

    if lista[index] == item_busca:
        return index

    return pesquisa(lista, item_busca, index + 1)

with open("Estrutura_dados/aula_arvore_binaria/numeros.txt", "r") as arquivo:
    lista = [int(linha.strip()) for linha in arquivo]


alvo = 7
resultado = pesquisa(lista, alvo)

if resultado == -1:
    print('item não existe')
else:
    print("posição", resultado)