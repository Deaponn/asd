# DFS search algorithm
# for graph represented as list of neighbours


def DFS(G):
    n = len(G)
    times = [-1] * n
    parent = [-1] * n
    time = 0
    def DFSVisit(v):
        nonlocal G
        nonlocal time
        nonlocal parent
        nonlocal times
        time += 1
        times[v] = time
        for w in G[v]:
            if times[w] == -1:
                parent[w] = v
                DFSVisit(w)
        time += 1
    for v in range(n):
        if times[v] == -1:
            DFSVisit(v)