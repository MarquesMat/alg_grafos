# Definir os vétices e as arestas do grafo
vertices = [1, 2, 3, 4, 5]
arestas = [(1, 2, 1), (1, 3, 3), (1, 5, 6), (2, 3, 1), (2, 4, 3), (3, 1, 1), (3, 2, 2), (3, 4, 1), (4, 1, 3), (4, 5, 2), (5, 4, 1)]
# (u, v, p) --> u alcança v com peso p

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
        print(f"{vertices[i]}  ",end="")
        #print(f" {linha}  ",end="")
        for item in linha:
            print(f"   {item}   ",end="")
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
    for i, vi in enumerate(vertices):
        for j, vj in enumerate(vertices):
            matriz[i][j] = get_min(matriz[i][j], matriz[i][indice-1] + matriz[indice-1][j])
    print_matriz(indice)


def matriz_distancia_inicial(indice):
    for i, vi in enumerate(vertices):
            for j, vj in enumerate(vertices):
                matriz[i][j] = get_peso(vi, vj)
    print_matriz(0)
    matriz_distancia(indice)


matriz_distancia_inicial(len(vertices))