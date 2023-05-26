# algorithm for finding bridges in an undirected graph
# graph is passed as an adjacency list



def find_bridges(G):
    n = len(G)
    bridge_parents = []
    times = [-1] * n
    parents = [-1] * n
    lows = [-1] * n
    time = 0
    def DFSVisit(v):
        nonlocal G
        nonlocal parents
        nonlocal lows
        nonlocal time
        nonlocal times
        time += 1
        times[v] = time
        for w in G[v]:
            if times[w] == -1:
                parents[w] = v
                DFSVisit(w)
        visited = [float("inf")]
        children_lows = [float("inf")]
        for w in G[v]:
            if times[w] != -1 and parents[v] != w:
                visited.append(times[w])
            if parents[w] == v:
                children_lows.append(lows[w])
        low_value = min(times[v], min(visited), min(children_lows))
        lows[v] = low_value
        if low_value == times[v] and parents[v] != -1:
            bridge_parents.append(parents[v])
    for v in range(n):
        if times[v] == -1:
            DFSVisit(v)
    return bridge_parents


graph = [
    [1, 5],
    [0, 7],
    [3, 4, 7],
    [2, 4],
    [2, 3],
    [0, 7, 6],
    [5],
    [1, 2, 5]
]


print(find_bridges(graph))
