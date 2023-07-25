# algorytmy przegladania grafow:
# BFS - wglab
# DFS - wszerz

from collections import deque


# dla grafu zadanego w postaci macierzy adjacencji
#   0 1 2 3 4 5
# 0 - 1 0 0 1 1
# 1 1 - 0 0 1 1
# 2 0 0 -...
# 3
# 4
# 5


def BFS(G):
    # G = (V, E)
    V = len(G)
    visited = [False for _ in range(V)]
    for v in range(V):
        if visited[v]: continue
        q = deque()
        q.push(0)
        while not q.empty():
            s = q.get()
            q.pop()
            visited[s] = True
            for i in range(V):
                if G[s][i]:
                    if not visited[i]:
                        q.push(i)


# dla grafu zadanego w postaci list sasiadow
# [
#   [1, 3],
#   [2, 3, 4, 5],
#   ...
# ]


def DFS(G):
    # G = (V, E)
    v = len(G)
    visited = [False for _ in range(v)]
    def visitDFS(G, s):
        nonlocal visited
        visited[s] = True
        for i in G[s]:
            if not visited[i]:
                visited[i] = True
                visitDFS(G, i)


# liczenie spojnych skladowych grafu:
# based on DFS

def DFS_spojne(G):
    # G = (V, E)
    v = len(G)
    visited = [False for _ in range(v)]
    skladowe = 0
    def visitDFS(G, s):
        nonlocal visited
        visited[s] = True
        for i in G[s]:
            if not visited[i]:
                visited[i] = True
                visitDFS(G, i)
    for i in range(v):
        if not visited[i]:
            skladowe += 1
            visitDFS(G, i)
    return skladowe


# sprawdzanie czy graf jest dwudzielny
# based on BFS
# przy odwiedzeniu wierzcholka kolorujemy go:
# 0 - nieodwiedzony
# 1 - niebieski
# 2 - czerwony
# jezeli dwoch sasiadow ma ten sam kolor, to graf nie jest dwudzielny

def is_dwudzielny(G):
    v = len(G)
    visited = [0 for _ in range(v)]
    q = deque()
    q.push(0)
    color = 1
    visited[0] = color
    while not q.empty():
        color = 3 - color
        s = q.get()
        q.pop()
        for i in range(v):
            if G[s][i]:
                if visited[i] == 0:
                    visited[i] = color
                elif visited[i] != color:   # kolor obecnego wierzcholka inny od koloru na ktory chcemy pomalowac
                                            # dwaj sasiedzi maja ten sam kolor
                    return False
                q.push(i)


# zad kolokwium 2017/2018
# znany operator telefonii komorkowej postanowil zakonczyc dzialalnosc w polsce
# jednym z glownych elementow procedury jest wylaczenie wszystkich nadajnikow bedacych grafem
# urzadzenia wylaczamy pojedynczo, ale w trakcie ich wylaczania graf caly czas musi byc spojny
# podaj algorytm zwracajacy kolejnosc wylaczania nadajnikow

# dany jest graf G zawierajacy n wierzcholkow
# zaproponuj algorytm ktory stwierdza czy w grafie G istnieje cykl zbudowany z 4 wierzcholkow

# mowimy ze wierzcholek t w grafie skierowanym jest unwiersalnym ujsciem jesli z kazdego wierzcholka
# istnieje krawedz do t, a z t nie wychodzi zadna krawedz
# szukamy czy istnieje t i go odnalezc

# zlozonosc n:
# startujemy z lewego gornego rogu
# jesli mamy 0 ide w prawo, jesli jest 1 ide w dol

def ujscie(G):
    v = len(G)
    x, y = 0, 0
    while x < v and y < v:
        if G[x][y] == 0:
            x += 1
        else:
            y += 1
    for i in range(v):
        if G[y][i] == 1:
            break
        if G[i][y] == 0 and i != y:
            break
    else:
        return y
    return None


# zadanie malejace krawedzie
# graf ma v wierzcholkow i e krawedzi o wagach ze zbioru { 1..e }
# zaproponuj algorytm ktory sprawdza czy istnieje sciezka od zadanych x do y
# w ktorej przechodzimy po krawedziach o malejacych wagach

# DFS ale idziemy dalej tylko jesli nastepna krawedz ma mniejsza wage niz poprzednia


# dana jest mapa krajow. kierowca chce przejechac z miasta X do Y
# niestety niektore drogi sa platne 1 (albo 0 gdy przejazd jest darmowy)
# szukamy najtanszej drogi prowadzacej z X do Y

# jezeli utworzymy kolejke w ktorej wierzcholki o koszcie przejazdu na nie 0 wrzucamy na poczatek, a 1 na koniec
# znajdziemy najtansza droge
