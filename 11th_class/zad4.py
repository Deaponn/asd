# sciezka w drzewie
# kazdy wierzcholek drzewa ma pewna wartosc, ktora rowniez moze byc ujemna
# szukamy sciezke z dowolnego wierzcholka do dowolnego wierczcholka o maksymalnej sumie wartosci

# trzymamy tablice maksow
# schodze rekurencyjnie do lisci, w kazdym lisciu sciezka to 0
# wracajac do rodzica sprawdzamy czy wartosc dziecka jest wieksza od rodzica

def path(G, root):
    max = 0
    
    maxes = [0 for _ in range(len(G))]
    
    def rek(curr, prev):
        nonlocal max
        
        for child, val in G[curr]:
            if child != prev:
                rek(child, curr)
                
                child_max = maxes[child] + val
                if child_max + maxes[curr] > max:
                    max = child_max + maxes[curr]
                
                if child_max > maxes[curr]:
                    maxes[curr] = child_max
    
    rek(root, None)
    
    return max
    

G = [[(1, 10), (2, 3), (3, 6)],
     [],
     [(7, 4)],
     [(5, 12), (6, -8)],
     [],
     [],
     [(7, 40)],
     []]
print(path(G, 0))