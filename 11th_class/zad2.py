# glodna zaba

# mamy liste od 0 do n-1
# zaba skacze po polach z tej listy
# A[i] to wartosc przekaski na danym polu
# skok z pola A[i] do A[j] kosztuje j-i
# szukamy minimalnej ilosci skokow aby przejsc na koniec tablicy

# f(i, t) - minimalna liczba skokow z pola i na pole koncowe, przy energii na skoki o wartosci t

# z memoizacja:
DP = dict()

def frog(i, energy, C):
    global DP
    # print(i, energy, energy + i, len(C))
    if energy + i >= len(C):
        return 1
    if i >= len(C):
        return float("inf")
    key = (i, energy) 
    if key in DP:
        return DP[key]
    jumps = [frog(i + x, energy - x + C[i + x], C) for x in range(1, min(energy - i, len(C) - i - 1))]
    if len(jumps) == 0:
        jumps = [float("inf")]
    lowest_jumps = min(jumps)
    DP[key] = lowest_jumps + 1
    return lowest_jumps + 1

def frog(i, energy, C):
    # print(i, energy, energy + i, len(C))
    if energy + i >= len(C):
        return 1
    if i >= len(C):
        return float("inf")
    jumps = [frog(i + x, energy - x + C[i + x], C) for x in range(1, min(energy - i, len(C) - i - 1))]
    if len(jumps) == 0:
        jumps = [float("inf")]
    lowest_jumps = min(jumps)
    return lowest_jumps + 1

lilypads = [5, 5, 0, 0, 0, 0, 0, 0, 0, 0]

print(frog(0, lilypads[0], lilypads))

# x = len(C) - i - 1