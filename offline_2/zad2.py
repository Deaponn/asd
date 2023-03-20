# Bartosz Sajecki

# algorytm dziala, poniewaz kolejnosc zbierania sniegu nie ma znaczenia
# pod warunkiem, ze wybierzemy najkorzystniejsze kupki sniegu
# tzn, ze jesli najlepszymi kupkami bedzie 100 oraz 97
# to nie ma znaczenia czy zbierzemy 100 a potem 96, czy 97 a potem 99
# dzieki temu mozna zaniedbac kolejnosc zbierania kupek sniegu
# i skupic sie na tym aby wybrac odpowiednie kupki
# a w tym pomaga posortowanie tablicy

from zad2testy import runtests


def quick_sort(T, start, end):
    if end - start <= 1:
        return
    divider = T[end - 1]
    last_bigger_idx = start
    for x in range(start, end):
        if T[x] >= divider:
            tmp = T[x]
            T[x] = T[last_bigger_idx]
            T[last_bigger_idx] = tmp
            last_bigger_idx += 1
    quick_sort(T, start, last_bigger_idx - 1)
    # this bit of code makes it 12x more performant
    # it checks if the array is sorted enough
    # because we need only the biggest snow piles
    # and dont care about the order of the small ones
    if last_bigger_idx > T[last_bigger_idx - 1]:
        return
    quick_sort(T, last_bigger_idx, end)


def snow( S ):
    output = 0
    day = 0
    quick_sort(S, 0, len(S))
    while S[day] > day:
        output += S[day] - day
        day += 1
    return output

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
