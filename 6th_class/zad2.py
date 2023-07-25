# wierzcholek v nazywamy dobrym poczatkiem, 
# jesli kazdy inny wierzcholek mozna osiagnac 
# idac po krawedziach wychodzacych z dobrego poczatku

# zwiazane ze skladowymi silnie spojnymi

# sposob 1
# odwracamy krawedzie, wtedy dobry poczatek stanie sie ujsciem
# dla odwroconego grafu szukamy silnych spojnych skladowych
# kazdy wierzcholek w ostatniej (topologicznie) spojnej skladowej jest dobrym poczatkiem

# sposob 2
# robimy DFS dla losowego wierzcholka
# nastepnie robimy DFS z wierzcholka o najwiekszym time

# zakladamy, ze graf jest spojny

def good_beginning(G):
    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    times = [0 for _ in range(n)]
    top = []
    def dfs(G, s):
        nonlocal time
        nonlocal times
        nonlocal visited
        visited[s] = True
        time += 1
        for v in G[s]:
            if not visited[v]:
                dfs(G, v)
        time += 1
        times[s] = time
        top.append(s)
    for v in range(n):
        dfs(G, n)
    max_idx = 0
    for i in range(1, n):
        if times[i] > times[max_idx]:
            max_idx = i
    visited = [False for _ in range(n)]
    dfs(G, max_idx)
    for v in range(n):
        if not v:
            return False
    return True
    