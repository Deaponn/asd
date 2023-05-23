# sort graph topologically
# graph is given in a form of list of neighbours


def topologic_sort(G):
    n = len(G)
    visited = [False] * n
    parent = [-1] * n
    output = []
    def DFSVisit(v):
        nonlocal G
        nonlocal parent
        nonlocal visited
        visited[v] = True
        for w in G[v]:
            if not visited[w]:
                parent[w] = v
                DFSVisit(w)
        output.append(v)
    for v in range(n):
        if not visited[v]:
            DFSVisit(v)
    return output[::-1]