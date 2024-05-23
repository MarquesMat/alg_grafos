# Definir os vétices e as arestas do grafo
# (u, v, p) --> u alcança v com peso p

# PRIMEIRO GRAFO (SLIDES)
vertices = [1, 2, 3, 4, 5]
arestas = [(1, 2, 1), (1, 3, 3), (1, 5, 6), (2, 3, 1), (2, 4, 3), (3, 1, 1), (3, 2, 2), (3, 4, 1), (4, 1, 3), (4, 5, 2), (5, 4, 1)]

# SEGUNDO GRAFO (PESO NEGATIVO)
#vertices = [1, 2, 3, 4, 5, 6]
#arestas = [(1, 2, 1), (2, 3, 1), (2, 4, 3), (2, 5, 2), (3, 1, 3), (3, 4, 2), (4, 6, 2), (5, 4, -3), (6, 5, 3)]

# TERCEIRO GRAFO (PESO NEGATIVO)
vertices = ["A", "B", "C", "D", "S"]
arestas = [("A", "B", 8), ("A", "C", 5), ("A", "D", -4), ("B", "C", -3), ("B", "D", 9), ("C", "A", -2), ("D", "C", 7), ("D", "S", 2), ("S", "A", 6), ("S", "B", 7)]

# A variável 'infinito' recebe o maior valor possível no Python
infinito = float('inf')

# Iniciando a matriz de distâncias (D) com o tamanho NxN, no qual N é a quantidade de vértices
matriz = [[-1 for _ in range(len(vertices))] for _ in range(len(vertices))]

def print_matriz(indice):
    print(f"\nD{indice}")
    for v in vertices:
        print(f"      {v}",end="")
    print("")

    for i, linha in enumerate(matriz):
        print(f"{vertices[i]}     ",end="")
        #print(f" {linha}  ",end="")
        for item in linha:
            print(f"{item}",end="")
            for j in range(7-len(str(item))):
                print(" ",end="")
        print("")


def get_min(x, y):
    if x > y:
        return y
    return x


def get_peso(vi, vj):
    if vi == vj:
        return 0
    for aresta in arestas:
        if vi == aresta[0] and vj == aresta[1]:
            return aresta[2]
    return infinito


def matriz_distancia(indice):
    if indice > 1:
        matriz_distancia(indice-1)
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            matriz[i][j] = get_min(matriz[i][j], matriz[i][indice-1] + matriz[indice-1][j])
    print_matriz(indice)


def matriz_distancia_inicial(indice):
    for i, vi in enumerate(vertices):
            for j, vj in enumerate(vertices):
                matriz[i][j] = get_peso(vi, vj)
    print_matriz(0)
    matriz_distancia(indice)


matriz_distancia_inicial(len(vertices))
