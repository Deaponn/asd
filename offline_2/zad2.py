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


def insertion_sort(T, start, end):
    n = end - start + 1
    output = [0] * n
    for idx in range(n):
        number = T[start + idx]
        for insert in range(n - 1, -1, -1):
            if number > output[insert - 1]:
                output[insert] = output[insert - 1]
            else:
                output[insert] = number
                break
            if insert == 0:
                output[0] = number
    return output


def merge(T, S):
    n = len(T)
    m = len(S)
    start_1st = 0
    start_2nd = 0
    output = [0] * (n + m)
    current_idx = 0
    while start_1st < n and start_2nd < m:
        if T[start_1st] > S[start_2nd]:
            output[current_idx] = T[start_1st]
            start_1st += 1
        else:
            output[current_idx] = S[start_2nd]
            start_2nd += 1
        current_idx += 1
    while start_1st < n:
        output[current_idx] = T[start_1st]
        start_1st += 1
        current_idx += 1
    while start_2nd < m:
        output[current_idx] = S[start_2nd]
        start_2nd += 1
        current_idx += 1
    return output


def merge_sort(T, start, end):
    n = end - start
    # standard merge_sort:
    # if n <= 0:
    #     return [T[start]]

    # below code optimizes from runtime 2.6s down to 2.3s (on my PC)
    # if n <= 0:
    #     return [T[start]]
    # if n == 1:
    #     if T[start] >= T[end]:
    #         return [T[start], T[end]]
    #     else:
    #         return [T[end], T[start]]

    # insertion sort for short arrays:
    # for small n this has no effect to the runtime
    if n < 41:
        T = insertion_sort(T, start, end)
        return T
    middle = start + n // 2
    left = merge_sort(T, start, middle)
    right = merge_sort(T, middle + 1, end)
    return merge(left, right)



def snow( S ):
    output = 0
    day = 0
    S = merge_sort(S, 0, len(S) - 1)
    # quick_sort(S, 0, len(S))
    while S[day] > day:
        output += S[day] - day
        day += 1
    return output

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
