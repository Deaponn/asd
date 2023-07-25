# szukanie sciezki Eulera w DAG
# robimy DFS, ale pomijamy w przechodzeniu krawedzie po ktorych juz przeszlismy

def find_euler(G):
    n = len(G)
    eulers = []

    def dfs(G, s):
        nonlocal eulers
        for v in range(n):
            if G[s][v] == 1:
                G[s][v] = G[v][s] = 0
                dfs(G, v)
        eulers.append(s)
