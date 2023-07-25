# sprawdzanie czy istnieje sciezka Hamiltona w DAG (acykliczny graf skierowany)
# nalezy posortowac topologicznie ten graf
# w posortowanym grafie powinna byc krawedz miedzy "sasiednimi" wierzcholkami

# algorytm sortowania topologicznego polega na DFS

def find_hamilton(G):
    n = len(G)
    visited = [False for _ in range(n)]
    top = []
    def dfs(G, s):
        nonlocal visited
        nonlocal top
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                dfs(G, v)
        top.append(s)
    dfs(G, 0)
    for i in range(1, n):
        if not top[i - 1] in G[i]:
            return False
    return True
