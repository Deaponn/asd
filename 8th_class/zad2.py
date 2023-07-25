# zaimplementuj algorytm kruskalla

class FindUnion:
    def __init__(self, length):
        self.parents = [x for x in range(length)]
        self.ranks = [0 for _ in range(length)]

    def find(self, member):
        if self.parents[member] != member:
            self.parents[member] = self.find(self.parents[member])
        return self.parents[member]
    
    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)
        if self.ranks[first_root] > self.ranks[second_root]:
            self.parents[second_root] = first_root
        else:
            self.parents[first_root] = second_root
            if self.ranks[first_root] == self.ranks[second_root]:
                self.ranks[second_root] += 1
    


def kruskall(G):
    n = len(G)
    # majac macierz, przerabiamy ja na liste krawedzi
    # a potem sortujemy rosnaco
    # dolaczamy krawedzie od najmniejszej, sprawdzajac czy ich wszyscy czlonkowie maja innych reprezentantow
