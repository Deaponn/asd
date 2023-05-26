# implementation of algorithm used to find strongly connected components of the graph
# graph is given in a form of adjacency list



def DFS(G):
    n = len(G)
    visited = [False] * n
    times = [-1] * n
    parent = [-1] * n
    time = 0
    def DFSVisit(v):
        nonlocal G
        nonlocal time
        nonlocal parent
        nonlocal times
        time += 1
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                parent[w] = v
                DFSVisit(w)
        times[v] = (v, time)
        time += 1
    for v in range(n):
        if times[v] == -1:
            DFSVisit(v)
    return times


def DFS_connected(G, times):
    n = len(G)
    output = []
    visited = [False] * n
    connected_idx = 0
    def DFSVisit(v):
        nonlocal G
        nonlocal visited
        visited[v] = True
        for w in G[v]:
            if not visited[w]:
                DFSVisit(w)
        output[connected_idx].append(v)
    for v, _ in times:
        if not visited[v]:
            output.append([])
            DFSVisit(v)
            connected_idx += 1
    return output


def strongly_connected_components(G):
    n = len(G)
    inverted_graph = [[] for _ in range(n)]
    for v in range(n):
        for w in G[v]:
            inverted_graph[w].append(v)
    first_DFS_times = DFS(G)
    first_DFS_times.sort(key=lambda vertex: vertex[1], reverse=True)
    strongly_connected_components_list = DFS_connected(inverted_graph, first_DFS_times)
    return strongly_connected_components_list


graph = [
    [1],
    [2],
    [0, 3, 10],
    [4, 6],
    [5],
    [3],
    [5],
    [5, 8],
    [3, 9],
    [10],
    [7]
]


reversed_graph = [
    [2], 
    [0], 
    [1], 
    [2, 5, 8], 
    [3], 
    [4, 6, 7], 
    [3], 
    [10], 
    [7], 
    [8], 
    [2, 9]
]


print(strongly_connected_components(graph))
print(strongly_connected_components(reversed_graph))