# domkniecie przechodnie
# algorytm obliczajacy domkniecie przechodnie dla grafu skierowanego w postaci macierzy
# domkniecie przechodnie jest to graf na zbiorze tych samych wierzcholkow,
# gdzie w domknieciu przechodnim grafu krawedz miedzy u oraz v istnieje tylko,
# gdy w wejsciowym grafie istnieje sciezka z u do v

# jest to na zastosowanie algorytmu floyda warshalla

# zakladamy, ze na przekatnych i tam gdzie nie ma krawedzi juz od razu wpisane sa zera
def floyd_warshall(G):
    n = len(G)
    for t in range(n):
        for x in range(x):
            for y in range(n):
                G[x][y] = min(G[x][y], G[x][t] + G[t][y])
    
    output = G.deepcopy()
    for x in range(n):
        for y in range(n):
            output[x][y] = 0 if output[x][y] == float("inf") else 1
    return output